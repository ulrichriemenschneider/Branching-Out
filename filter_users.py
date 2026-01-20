import json


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def validate_age():
    while True:
        try:
            age = int(input("Enter a age to filter users: ").strip())
            if 0 <= age <= 120:
                return age
            else:
                print("Error: Age must be between 0 and 120.")
        except ValueError:
            print("Error: Please enter an integer.")


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? (Currently, only 'name', 'email' and 'age' is supported): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = validate_age()
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
