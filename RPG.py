import random
PlayerHP = 50
NpcHP = 30


print("You encounter an enemy npc ")
while NpcHP > 0 and PlayerHP > 0:
    PlayerAttack = random.randint(1, 10)
    PlayerBlock = random.randint(0, 10)
    PlayerHeal = random.randint(1, 10)
    NpcAttack = random.randint(0, 10)
    choice = int(input("What is you choice to 1) Attack 2) Block 3) Heal "))
    if choice == 1:
        NpcHP -= PlayerAttack
        print("Enemy has "+str(NpcHP)+" HP left")
        print("You did "+str(PlayerAttack)+" damage")
    elif choice == 2:
        print("Enemy begins to attack")
        if PlayerBlock < NpcAttack:
            damage_taken = NpcAttack - PlayerBlock
            PlayerHP -= damage_taken
            print("The attack went through your block and you took "+str(damage_taken)+" damage")
            print("HP left "+str(PlayerHP))
        else:
            print("You took no damage from the enemy")
    elif choice == 3:
        print("You began to heal yourself")
        if PlayerHP >= 50:
            print("Your already at full HP")
        elif PlayerHP < 50:
            heal_amount = min(50 - PlayerHP, PlayerHeal)
            PlayerHP += heal_amount
            print("You healed for "+str(heal_amount))
            print("You are at "+str(PlayerHP))
        else:
            print("Failed to heal")
    else:
        print("Wrong input")
    if NpcHP <= 0:
        print("You defeated the enemy NPC!")
        break
    if PlayerHP <= 0:
        print("You were defeated")
        break



