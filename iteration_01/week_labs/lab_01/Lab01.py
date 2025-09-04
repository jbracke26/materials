# Lab 01

class Lab01: 
    usercount = int(2)
    for n in range(1, usercount):
        userinfo = {
            {
                "userid": str(n),
                "name": input("What is your name?"),
                "age": int(input("What is your age?")),
                "languages": int(input("How many languages do you know?")),
            }
        }

        print(f"Hello {userinfo['name']}, welcome to the program. ")

        if userinfo["age"] > 35:
            print("You are getting old.")
        if userinfo["age"] < 25:
            print("You cannot rent a car.")
        if userinfo["age"] < 18:
            print("You cannot vote.")
        if userinfo["age"] < 13:
            print("You cannot sit in the passenger seat of a car.")

        if userinfo["languages"] > 1:
            for i in range(1, userinfo["languages"] + 1):
                userinfo["languages" + str(i)] = input(
                    "What is language number " + str(i) + " that you know?"
                )

        if input("Would you like to enter another person's information? (Y/N)") == "Y":
            usercount = usercount + 1
        else:
            break

    print(userinfo)
