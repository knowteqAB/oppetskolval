# -*- coding: utf-8 -*-
import pytest
from oppetskolval.model.pupil import Pupil, Assignment
from oppetskolval.model.location import Location


@pytest.fixture(scope="session")
def pupil() -> Pupil:
    pupil = Pupil("121212-1212",
                  "Kalle",
                  "Andersson",
                  Location("home address", "Storgatan 1, Skolstaden", 12.01, 13.01),
                  ["skola1", "skola2"],
                  {'skola1': 123.45, 'skola2': 234.56},
                  {'skola1': 111, 'skola2': 222})
    return pupil


def test_init():
    pupil = Pupil("121212-1212",
                  "Kalle",
                  "Andersson",
                  Location("home address", "Storgatan 1, Skolstaden", 12.01, 13.01),
                  ["skola1", "skola2"],
                  {'skola1': 123.45, 'skola2': 234.56},
                  {'skola1': 111, 'skola2': 222})

    assert pupil.person_id == "121212-1212"
    assert pupil.first_name == "Kalle"
    assert pupil.last_name == "Andersson"
    assert pupil.location.address == "Storgatan 1, Skolstaden"
    assert pupil.location.latitude == 12.01
    assert pupil.location.longitude == 13.01
    assert pupil.selections == ["skola1", "skola2"]
    assert pupil.dist_map == {'skola1': 123.45, 'skola2': 234.56}
    assert pupil.score_map == {'skola1': 111, 'skola2': 222}

    assert isinstance(pupil.assignment, Assignment)


def test_display_name(pupil):
    assert pupil.display_name == "Kalle Andersson"


def test_choice_priority(pupil):
    pupil.selections = ['1', '2', '3']
    assert pupil.choice_priority('1') == 0
    assert pupil.choice_priority('2') == 1
    assert pupil.choice_priority('3') == 2


def test_distance_to_guarantee_school(pupil):
    pupil.assignment.guarantee_school = "skola1"
    assert pupil.distance_to_guarantee_school() == 123.45


def test_distance_to_guarantee_school_shall_throw_if_no_guarantee_school_defined(pupil):
    pupil.assignment.guarantee_school = None
    with pytest.raises(ValueError, match=r"No guarantee school defined"):
        pupil.distance_to_guarantee_school()


def test_distance_to_guarantee_school_shall_throw_if_guarantee_school_not_in_dist_map(pupil):
    pupil.assignment.guarantee_school = "dummy"
    with pytest.raises(ValueError, match=r"Guarantee school could not be found in dist_map"):
        pupil.distance_to_guarantee_school()


def test_selections_better_than_assigned_school(pupil):
    pupil.selections = ['skola1', 'skola2', 'skola3', 'skola4']
    pupil.assignment.assigned_school = 'skola3'

    assert pupil.selections_better_than_assigned_school() == ['skola1', 'skola2']


def test_selections_better_than_assigned_school_when_no_school_assigned(pupil):
    pupil.selections = ['skola1', 'skola2', 'skola3', 'skola4']

    pupil.assignment.assigned_school = None
    with pytest.raises(ValueError, match=r"No school assigned for pupil"):
        pupil.selections_better_than_assigned_school()

    pupil.assignment.assigned_school = ""
    with pytest.raises(ValueError, match=r"No school assigned for pupil"):
        pupil.selections_better_than_assigned_school()
