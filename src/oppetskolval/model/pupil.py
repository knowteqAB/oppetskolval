# -*- coding: utf-8 -*-
from typing import List, Dict

from oppetskolval.model.location import Location


class Assignment(object):
    """
    A data class used to store assignment information.
    """
    def __init__(self):

        self.assignment_note = ""
        """Free text note"""
        self.assigned_school: str = ""
        """The current assigned school."""
        self.guarantee_school: str = ""
        """The guaranteed worst case assignment"""
        self.route_urls: Dict = {}
        """Dictionary intended to store urls containing routing information. The information can be used
        when generating proof of legality related to a pupils assignment
        """
        self.route_tacks: Dict = {}
        """Dictionary intended to store data related to routing. The information can be used
        when generating proof of legality related to a pupils assignment
        """


class Pupil(object):
    """
    A class representing a pupil in a school district

    Attributes
    ---------
    person_id : str
        A unique identifier. This could be the pupils person id, or some other identifier.
    first_name : str
        The pupils first name.
    last_name : str
        The pupils last name.
    location : Location
        The pupils location to be used in location based assignment algorithms.
    selections : list of str
        The selected schools, by school name, in prioritized order.
    dist_map : dict of (str,float)
        The distance-to-school lookup map for the pupil.

        - *Key*: school name
        - *Value*: distance in meter to school
    score_map : dict of (str,float)
        The school-score lookup map for the pupil. This map can be used in top trading cycle based algorithms when
        pupils compete against each other in the assignment process.

        - *Key*: school name
        - *Value*: score when applying to school
    """

    def __init__(self,
                 person_id,
                 first_name="",
                 last_name="",
                 location=None,
                 selections=None,
                 dist_map=None,
                 score_map=None):

        self.person_id: str = person_id
        """Pupils person id or a unique identifier"""
        self.first_name = first_name
        """The pupils first name."""
        self.last_name = last_name
        """The pupils last name."""
        self.location: Location = location
        """The pupils location to be used in location based assignment algorithms."""
        self.selections: List = selections if selections is not None else []
        """The selected schools, by school name, in prioritized order."""
        self.dist_map: Dict = {} if dist_map is None else dist_map
        """The distance-to-school lookup map for the pupil."""
        self.score_map: Dict = {} if score_map is None else score_map
        """The school-score lookup map for the pupil."""
        self.assignment: Assignment = Assignment()
        """Assignment info for pupil"""

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    @property
    def display_name(self):
        """The pupils name as 'first_name last_name'"""
        return f"{self.first_name} {self.last_name}"

    @property
    def has_selections(self) -> bool:
        """Returns True if the pupil has any selected schools"""
        return len(self.selections) == 0

    def choice_priority(self, school: str):
        """Returns the pupils priority for the school

        Parameters
        ----------
        school : str
            School name
        """
        if school not in self.selections:
            return -1
        return self.selections.index(school)

    def schools_in_dist_order(self):
        """Gets the schools in distance order for the pupil."""
        schools_with_dist = [(k, v) for k, v in self.dist_map.items()]
        ordered_schools = sorted(schools_with_dist, key=lambda x: x[1])
        return [x[0] for x in ordered_schools]

    def distance_to_guarantee_school(self):
        if self.assignment.guarantee_school is None:
            raise ValueError("No guarantee school defined")
        if self.assignment.guarantee_school not in self.dist_map.keys():
            raise ValueError("Guarantee school could not be found in dist_map")
        return self.dist_map[self.assignment.guarantee_school]

    def selections_better_than_assigned_school(self):
        if not self.assignment.assigned_school:
            raise ValueError("No school assigned for pupil")

        assigned_school_index = self.selections.index(self.assignment.assigned_school)
        return self.selections[:assigned_school_index]

    def set_guarantee_school(self, school, score_for_guarantee_school=1000000.0):
        """
        Sets the guarantee school for the pupil. This method can be used by assignment algorithms that
        assure some worst case assignment for each pupil.

        Parameters
        ----------
        school : str
            The school to be set as guarantee school
        score_for_guarantee_school : float
            The score to be set in the score map for the guarantee school.
        """
        assert self.assignment.guarantee_school is None, "This pupil already has a guarantee school"
        self.assignment.guarantee_school = school
        guarantee_name = self.assignment.guarantee_school
        guarantee_dist = self.dist_map[guarantee_name]
        for s in self.dist_map:
            if s != guarantee_name:
                self.score_map[s] = guarantee_dist - self.dist_map[s]
            else:
                self.score_map[s] = score_for_guarantee_school

    def describe(self):
        d = [
            "Namn: " + self.display_name,
            "Närmsta skola: " + min(self.dist_map, key=self.dist_map.get),
            "Garanti-skola: " + self.assignment.guarantee_school,
            "Distanser: " + str(self.dist_map),
            "Scorer:" + str(self.score_map)
        ]

        return "\n".join(d)

    def dump(self):
        return {
            'name': self.display_name,
            'person_id': self.person_id,
            'selections': self.selections,
            'dist_map': self.dist_map,
            'geocode': (self.location.latitude, self.location.longitude),
            'score_map': self.score_map,
            'assignment_note': self.assignment.assignment_note,
            'address': self.location.address
        }
