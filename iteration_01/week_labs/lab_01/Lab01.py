class User:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.multilingual = False
        self.languages = []

    def get_info(self):
        self.name = input("What is your name? ")
        self.age = int(input("How old are you? "))
        multilingual_input = input("Are you multilingual? (yes/no): ").lower()
        self.multilingual = multilingual_input in ["yes", "y"]

        print(f"Hello {self.name}! Welcome to the program!")

        if self.age < 13:
            print("You cannot sit in the passenger seat of a car.")
        if self.age < 18:
            print("You cannot vote.")
        if self.age < 25:
            print("You cannot rent a car.")
        if self.age > 35:
            print("You are getting old...")

        if self.multilingual:
            num_languages = int(input("How many languages do you speak? "))
            for i in range(num_languages):
                language = input(f"Enter language {i + 1}: ")
                self.languages.append(language)
            print(f"Languages you speak: {', '.join(self.languages)}")
        else:
            desired_language = input("Enter a language you wish to learn: ")
            self.languages.append(desired_language)
            print(f"You wish to learn: {desired_language}")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "multilingual": self.multilingual,
            "languages": self.languages,
        }


all_users = []

while True:
    user = User()
    user.get_info()
    all_users.append(user.to_dict())

    continue_input = input(
        "Would another user like to enter their information? (yes/no): "
    ).lower()
    if continue_input not in ["yes", "y"]:
        break

print("All user information:")
for user in all_users:
    print(user)
