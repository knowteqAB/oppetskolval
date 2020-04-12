# -*- coding: utf-8 -*-
from oppetskolval.model.pupil import Pupil
from oppetskolval.model.location import Location, Address


def parse_pupils(filename, school_district):
    """Parse pupils in knowteq pupil format

        Parameters
        ----------
        filename : str
            path to pupil csv file
        school_district : SchoolDistrict
            school district instance to populate pupils in
        
        CSV file format
        ---------------
        Delimiter: ;
        First row: header row

        Columns:
        0: person_id:          person id
        1: first_name:         first name
        2: last_name           last name
        3: street_address:     street address
        4: zipcode:            ZIP code
        5: postal_address:     Area
        6: choice_1:           First school choice
        7: choice_2:           Second school choice
        8: choice_3:           Third school choice
        9: sibling_priority:   School name where sibling priority apply
    """
    assert len(school_district.pupils) == 0, "Pupil list must be empty"
    with open(filename, 'r') as f:
        rows = f.readlines()
        data = [x.split(';') for x in rows[1:]]

    for p in data:
        selections = [p[6], p[7], p[8]] if len(p) > 8 else []
        address = Address(p[3], p[4], p[5])
        pupil = Pupil(p[0], p[1], p[2], Location("home", address), selections=selections)
        school_district.pupils.append(pupil)
