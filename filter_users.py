import json


def load_json():
    """ Load users.json and returns it """
    with open("users.json", "r") as file:
        return json.load(file)


def print_user(filtered_users: list[dict]):
    """ Get a list with user-data and prints it """
    for user in filtered_users:
        print(user)


def filter_users_by_email(email: str):
    """ filter users by email and prints them """
    users = load_json()

    filtered_users = [user for user in users if user["email"].lower()
                      == email.lower()]

    print_user(filtered_users)


def filter_by_age(age: int):
    """ filter users by age and prints them """
    users = load_json()

    filtered_users = [user for user in users if user["age"] == age]

    print_user(filtered_users)


def filter_users_by_name(name: str):
    """ filter users by name and prints them """
    users = load_json()

    filtered_users = [user for user in users if user["name"].lower()
                      == name.lower()]

    print_user(filtered_users)


def validated_age() -> int:
    """ ask for input of age until input is valide and returns it """
    while True:
        try:
            age = int(input("Enter a age to filter users: ").strip())
            if 0 <= age <= 120:
                return age
            else:
                print("Error: Age must be between 0 and 120.")
        except ValueError:
            print("Error: Please enter an integer.")


def validated_name() -> str:
    """ ask for input of name until input is valide and returns it """
    while True:
        try:
            name = input("Enter a name to filter users: ").strip()

            if not name:
                raise ValueError("The name cannot be empty.")

            if not name.isalpha():
                raise ValueError("The name may only contain letters.")

            if len(name) < 2:
                raise ValueError("The name is too short.")

            return name

        except ValueError as error:
            print(f"Error: {error}")


def validated_email() -> str:
    """ ask for input of email until input is valide and returns it """
    while True:
        try:
            email = input("Enter a email to filter users: ").strip()

            if not email:
                raise ValueError("The email address must not be empty.")

            if email.count("@") != 1:
                raise ValueError(
                    "The email address must contain exactly one @ symbol.")

            name, domain = email.split("@")

            if not name or not domain:
                raise ValueError("A part is missing before or after the @.")

            if "." not in domain:
                raise ValueError(
                    "The domain must contain at least one dot.")

            return email

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? (Currently, only 'name', "
            "'email' and 'age' is supported): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = validated_name()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = validated_age()
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = validated_email()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
