# -*- coding: utf-8 -*-
from typing import List
from oppetskolval.model.pupil import Pupil
from oppetskolval.model.location import Location


class School(object):

    def __init__(self, name, locations, max_pupils):
        assert len([x for x in locations if not x.name]) == 0, "Locations used for schools must have a name"

        self.name = name
        """School name"""
        self.max_pupils = max_pupils
        """Max number of pupils that cna be assigned to the school"""
        self.locations: List[Location] = locations
        """The school location. This can be one or many locations.

         Locations used for schools must have a name.

         For distance based algorithms,multiple locations (school entry points) can be used to improve fairness in the
         assignments. The assignment algorithm can use the shortest route to the school for a pupil which reduces the
         risk of routs being created around the school property. See [add link here] for more info."""

        self._pupils: List[Pupil] = []
        self._rejected_pupils = []

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def free_spots(self):
        """The number of pupils that can be assigned without removing some other pupil"""
        return self.max_pupils - len(self._pupils)

    def pupil_list(self):
        """Returns a list of pupils that are assigned to the school"""
        return [p for p in self._pupils]  # Makes a copy to protect the internal list of pupils

    def can_add_pupil(self, pupil: Pupil):
        """Checks if the pupil can be assigned to the school.

        This is true if the school is not full, or if the pupil has a higher score than some
        other pupil that is already assigned to the school
        """
        if self.free_spots() > 0:
            return True
        if min([x.score_map[self.name] for x in self._pupils]) < pupil.score_map[self.name]:
            return True
        return False

    @property
    def acceptance_list(self):
        """The list of assigned pupils in score order"""
        acceptance_list = []
        for p in self.pupil_list():
            acceptance_list.append((p, p.score_map[self.name]))
        acceptance_list = sorted(acceptance_list, key=lambda x: x[1], reverse=True)
        return acceptance_list

    @property
    def rejection_list(self):
        """The list of rejected pupils in score order"""
        rejection_list = [(p, p.score_map[self.name]) for p in self._rejected_pupils]
        return sorted(rejection_list, key=lambda x: x[1], reverse=True)

    def remove_pupil(self, pupil):
        assert pupil in self._pupils, "The pupil is not assigned to this school"
        assert pupil.assignment.assigned_school == self.name, \
            f"Data error. The pupil {pupil.person_id} is unaware of its current assignment {pupil.assignment.assignment_note}"
        pupil.assignment.assigned_school = None
        self._pupils.remove(pupil)

    def try_assign_pupil(self, pupil, note):
        """Adds the pupil to the school.

        Attributes
        ---------
        pupil : Pupil
            The pupil that shall be assigned to the school
        note : str
            Assignment note

        Returns
        -------
        True if the pupil could be added to the school. Else False.
        """
        if self.can_add_pupil(pupil):
            self._pupils.append(pupil)
            pupil.assignment.assigned_school = self.name

            if self.max_pupils - len(self._pupils) < 0:
                # kick out pupil with lowest score
                kick_out_pupil = min(self._pupils, key=lambda x: x.score_map[self.name])
                self.remove_pupil(kick_out_pupil)
                if pupil not in self._rejected_pupils:
                    self._rejected_pupils.append(kick_out_pupil)

            assert len(self._pupils) <= self.max_pupils, "School overflow!"
            return True

        if pupil not in self._rejected_pupils:
            self._rejected_pupils.append(pupil)
        return False
