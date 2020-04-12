# -*- coding: utf-8 -*-
from oppetskolval.model.school_district import SchoolDistrict
from oppetskolval.model.location import Location
from oppetskolval.model.school import School
from oppetskolval.model.pupil import Pupil


def test_get_school_by_name():
    sd = SchoolDistrict()
    school1 = School("school1", [Location("test", "test", 0, 0)], 2)
    school2 = School("school2", [Location("test", "test", 0, 0)], 2)
    sd.schools += [school1, school2]

    assert sd.get_school_by_name('school1') == school1
    assert sd.get_school_by_name('school2') == school2


def test_get_school_by_name__no_match_shall_return_none():
    sd = SchoolDistrict()
    school1 = School("school1", [Location("test", "test", 0, 0)], 2)
    school2 = School("school2", [Location("test", "test", 0, 0)], 2)
    sd.schools += [school1, school2]

    assert sd.get_school_by_name('school3') is None


def test_get_pupil_by_person_id():
    sd = SchoolDistrict()
    p1 = Pupil('1')
    p2 = Pupil('2')
    sd.pupils += [p1, p2]

    assert sd.get_pupil_by_person_id('1') == p1
    assert sd.get_pupil_by_person_id('2') == p2


def test_get_pupil_by_person_id__no_match_shall_return_none():
    sd = SchoolDistrict()
    p1 = Pupil('1')
    p2 = Pupil('2')
    sd.pupils += [p1, p2]

    assert sd.get_pupil_by_person_id('3') is None


def test_get_unassigned_pupils():
    sd = SchoolDistrict()
    p1 = Pupil('1')
    p2 = Pupil('2')
    school1 = School("school1", [Location("test", "test", 0, 0)], 2)
    school2 = School("school2", [Location("test", "test", 0, 0)], 2)

    sd.pupils += [p1, p2]
    sd.schools += [school1, school2]

    assert len(sd.get_unassigned_pupils()) == 2
    assert p1 in sd.get_unassigned_pupils()
    assert p2 in sd.get_unassigned_pupils()

