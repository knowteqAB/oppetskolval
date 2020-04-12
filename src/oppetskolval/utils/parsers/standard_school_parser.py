# -*- coding: utf-8 -*-
import json
from oppetskolval.model.school import School
from oppetskolval.model.location import Location


def parse_schools(filename, school_district):
    """Parse schools in knowteq school format

    Parameters:
        filename : str
            path to school json file
        school_district : SchoolDistrict
            schoolDistrict instance to populate schools in

        JSON file format
        ---------------
        [
            {
               'name' : 'school name',
               'max_pupils' : max pupils in school
               'entry_points : [
                   {
                       'name' : 'Entry point name'
                       'north' : XX.XXXXXX,
                       'east' : XX.XXXXXX,
                   }
               ]
            }
       ] 
    """
    assert len(school_district.schools) == 0, "School list must be empty"
    with open(filename) as f:
        data = json.load(f)
    
    for s in data:
        locations = [Location(ep['name'], latitude=ep['east'], longitude=ep['north']) for ep in s['entry_points']]
        school = School(s['name'], locations, s['max_pupils'])
        school.entry_points = s['entry_points']
        school_district.schools.append(school)
