from character.mycharacter import MyCharacter


def test_mycharacter():
    chara = MyCharacter(name="TestHero", health=100, mp=50, attack_point=20, skills=["Fireball", "Heal"])
    
    assert isinstance(chara, MyCharacter)
    assert chara.name == "TestHero"
    assert chara.health == 100
    assert chara.mp == 50
    assert chara.attack_point == 20
    assert chara.skills == ["Fireball", "Heal"]