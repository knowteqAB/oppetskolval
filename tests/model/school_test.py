# -*- coding: utf-8 -*-
from oppetskolval.model.school import School
from oppetskolval.model.pupil import Pupil
from oppetskolval.model.location import Location


def test_init():
    location = Location("test", "", 0, 0)
    school = School("school1", [location], 100)

    assert school.name == "school1"
    assert school.locations == [location]
    assert school.max_pupils == 100


def test_free_spots():
    school = School("school1", [Location("test", "test", 0, 0)], 100)
    assert school.free_spots() == 100
    school._pupils.append(Pupil('test'))
    assert school.free_spots() == 99


def test_pupil_list():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    school._pupils.append(p1)
    school._pupils.append(p2)

    pupil_list = school.pupil_list()

    assert p1 in pupil_list
    assert p2 in pupil_list


def test_can_add_pupil_when_free_spots():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    assert school.can_add_pupil(p1)


def test_can_add_pupil_when_no_free_spots_with_higher_score():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school._pupils.append(p1)
    school._pupils.append(p2)

    p3 = Pupil('3')
    p3.score_map['school1'] = 300
    assert school.can_add_pupil(p3)


def test_can_add_pupil_when_no_free_spots_with_lower_score():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school._pupils.append(p1)
    school._pupils.append(p2)

    p3 = Pupil('3')
    p3.score_map['school1'] = 10
    assert not school.can_add_pupil(p3)


def test_try_asiign_pupil_when_no_free_spots_with_higher_score():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school.try_assign_pupil(p1, 'test')
    school.try_assign_pupil(p2, 'test')

    p3 = Pupil('3')
    p3.score_map['school1'] = 300
    assert school.try_assign_pupil(p3, 'test')
    assert p3 in school.pupil_list()
    assert p3 not in [x[0] for x in school.rejection_list]


def test_try_assign_pupil_when_no_free_spots_with_lower_score():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school.try_assign_pupil(p1, 'test')
    school.try_assign_pupil(p2, 'test')

    p3 = Pupil('3')
    p3.score_map['school1'] = 10
    school.try_assign_pupil(p3, 'test')
    assert p3 not in school.pupil_list()
    assert p3 in [x[0] for x in school.rejection_list]


def test_acceptance_list():
    school = School("school1", [Location("test", "test", 0, 0)], 2)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school.try_assign_pupil(p1, 'test')
    school.try_assign_pupil(p2, 'test')

    assert len(school.acceptance_list) == 2
    assert school.acceptance_list[0] == (p2, 200)
    assert school.acceptance_list[1] == (p1, 100)


def test_rejection_list():
    school = School("school1", [Location("test", "test", 0, 0)], 1)
    p1 = Pupil('1')
    p2 = Pupil('2')
    p1.score_map['school1'] = 100
    p2.score_map['school1'] = 200
    school.try_assign_pupil(p1, 'test')
    school.try_assign_pupil(p2, 'test')

    assert len(school.rejection_list) == 1
    assert school.rejection_list[0] == (p1, 100)

