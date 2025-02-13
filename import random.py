#dado rpg
print("Bem vindo ao Dado virtual Amdice")
import random

def roll_dice(sides):
    return random.randint(1, sides)

# Menu de opções para o jogador
while True:
    print("\nChoose a dice to roll:")
    print("1. D4 (4 sides)")
    print("2. D6 (6 sides)")
    print("3. D8 (8 sides)")
    print("4. D10 (10 sides)")
    print("5. D12 (12 sides)")
    print("6. D20 (20 sides)")
    print("7. Exit")

    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        print(f"You rolled a D4 and got: {roll_dice(4)}")
    elif choice == "2":
        print(f"You rolled a D6 and got: {roll_dice(6)}")
    elif choice == "3":
        print(f"You rolled a D8 and got: {roll_dice(8)}")
    elif choice == "4":
        print(f"You rolled a D10 and got: {roll_dice(10)}")
    elif choice == "5":
        print(f"You rolled a D12 and got: {roll_dice(12)}")
    elif choice == "6":
        print(f"You rolled a D20 and got: {roll_dice(20)}")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")