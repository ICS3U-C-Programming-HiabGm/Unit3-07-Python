#Created by: Hiab G
# Date: Wed, Feb. 28th
# This program checks if you are older then 40 but younger than 25 


def main():
    # Get the player's guess
    try:
        player_age = int(input("Enter your age: "))

        if (player_age > 25 and player_age < 40): 
            print("You can date my grandchild!")
        else:
            print(f"You can not date my grandchild.")

# checks if a the input is valid 
    except Exception:
        player_guess = input("")  
        print(f"Please enter a valid number, {player_guess} is not a valid number")


if __name__ == "__main__":
    main()
