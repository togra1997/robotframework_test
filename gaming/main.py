from src.character import EnemyCharacter, MyCharacter


def main():
    mycharacter = MyCharacter(name="Hero", health=100, mp=50,attack_point=20, skills=["Fireball", "Heal"])
    enemy = EnemyCharacter(name="Goblin", health=80, mp=30, attack_point=15)
    print(f"Character Name: {mycharacter.skills}")
    


if __name__ == "__main__":
    main()
