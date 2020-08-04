from pet import Pet

def test_pet_class():
    p = Pet()
    assert isinstance(p, Pet)
    assert p.name == "molly"
    

def test_pet_has_name():
    p = Pet("fido")
    assert p.name == "fido"


def test_pet_has_details():
    d1 = {"age": 3, "sex": "female"}
    p1 = Pet(**d1)
    assert p1.name == "molly"
    assert p1.species == "dog"
    d2 = {"name": "frank", "species": "spider"}
    p2 = Pet(**d2)
    assert p2.name == "frank"
    assert p2.species == "spider"