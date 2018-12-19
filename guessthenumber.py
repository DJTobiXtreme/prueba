real_number = 2

guy_number = int(input("Guess the number between 1 and 6: "))

if guy_number == real_number:
    print("you won beach")
else:
    print("you lost try again")
    guy_number = int(input("Try again: "))
    if guy_number == real_number:
        print("you won beach")
    else:
        print("you lost try again")
        guy_number = int(input("Try again: "))
        if guy_number == real_number:
            print("you won beach")
        else:
            print("you lost try again")
            guy_number = int(input("Try again: "))
            if guy_number == real_number:
                print("You won beach")
            else:
                print("you lost try again")
                guy_number = int(input("Try again: "))
                if guy_number == real_number:
                    print("you won beach")
                else:
                    print("Game over")