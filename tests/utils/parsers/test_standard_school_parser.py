# -*- coding: utf-8 -*-
import os
import oppetskolval.utils.parsers.standard_school_parser as sp
from oppetskolval.model.school_district import SchoolDistrict


def test_parse_schools():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    testfile = os.path.join(dir_name, r'../../testdata/schools_1.json')
    assert os.path.exists(testfile), testfile
    school_district = SchoolDistrict()
    sp.parse_schools(testfile, school_district)

    assert len(school_district.schools) == 4
    solskolan = school_district.schools[0]
    assert solskolan.name == "Solskolan"
    assert solskolan.max_pupils == 2
    assert len(solskolan.locations) == 4

    assert solskolan.locations[0].name == "1"
    assert solskolan.locations[0].latitude == 17.89110
    assert solskolan.locations[0].longitude == 59.38045
