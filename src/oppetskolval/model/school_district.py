# -*- coding: utf-8 -*-
from typing import List
import pickle
import copy
from oppetskolval.model.pupil import Pupil
from oppetskolval.model.school import School


class SchoolDistrict(object):

    def __init__(self):
        self.schools: List[School] = []
        """List of schools in district"""
        self.pupils: List[Pupil] = []
        """List of pupils in district"""

    def clone(self):
        return copy.deepcopy(self)

    def get_school_by_name(self, school_name):
        return next((s for s in self.schools if s.name == school_name), None)

    def get_pupil_by_person_id(self, person_id):
        return next((p for p in self.pupils if p.person_id == person_id), None)

    def get_unassigned_pupils(self):
        return [p for p in self.pupils if not p.assignment.assigned_school]

    # --- backup restore ---
    def save(self, filename):
        with open(filename, 'wb') as pickle_out:
            pickle.dump(self, pickle_out)

    @staticmethod
    def open(filename):
        with open(filename, 'rb') as pickle_in:
            return pickle.load(pickle_in)
