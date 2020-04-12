# -*- coding: utf-8 -*-
import os
import oppetskolval.utils.parsers.standard_pupil_parser as pp
from oppetskolval.model.school_district import SchoolDistrict


def test_parse_pupils():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    testfile = os.path.join(dir_name, r'../../testdata/pupils_1.csv')
    assert os.path.exists(testfile), testfile
    school_district = SchoolDistrict()
    pp.parse_pupils(testfile, school_district)

    assert len(school_district.pupils) == 6
    frank = school_district.get_pupil_by_person_id("1")
    assert frank.person_id == "1"
    assert frank.display_name == "Frank Frankson"
    assert frank.location.address.street_address == "Gata 1"
    assert frank.location.address.zip_code == "12345"
    assert frank.location.address.city == "Storstan"
    assert frank.selections == ["Solskolan", "Regnskolan", "Blixtskolan"]
