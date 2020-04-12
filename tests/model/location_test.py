from oppetskolval.model.location import Location


def test_init():
    location = Location("test name", "test", 1.0, 2.0)
    assert location.name == "test name"
    assert location.address == "test"
    assert location.latitude == 1.0
    assert location.longitude == 2.0


def test_geocode():
    location = Location("test name", "test", 1.0, 2.0)
    assert location.geocode == (1.0, 2.0)
