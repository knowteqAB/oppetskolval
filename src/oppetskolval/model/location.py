# -*- coding: utf-8 -*-


class Address(object):
    """
        A class used to represent a street address

        Attributes
        ----------
        street_address : str
            Street address
        zip_code : str
            Zip code
        city : str
            City
    """
    def __init__(self, street_address: str, zip_code: str, city: str):
        self.street_address: str = street_address
        self.zip_code: str = zip_code
        self.city: str = city


class Location(object):
    """
        A class used to represent a location

        Attributes
        ----------
        address : str
            address string
        latitude : float
            latitude coordinate
        longitude : float
            longitude coordinate
        """
    def __init__(self, name: str, address: Address = None, latitude: float = 0.0, longitude: float = 0.0):
        self.name: str = name
        """The location name."""
        self.address: Address = address
        """Location address"""
        self.latitude: float = latitude
        """Location latitude. Default value 0.0"""
        self.longitude: float = longitude
        """Location longitude. Default value 0.0"""

    @property
    def geocode(self):
        """Location geocode as a lat,lon tuple"""
        return self.latitude, self.longitude
