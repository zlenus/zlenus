from module import Character
bob = Character()
def test_vitals():
    assert bob.vitals() == "Your health level is at 20"
def test_energy():
    assert bob.energy() == 20
def test_haveInjury():
    bob.haveInjury() == "Your health level has been lowered to 20"
def test_hurt():
    bob.hurt()
    assert bob.health == 10
    