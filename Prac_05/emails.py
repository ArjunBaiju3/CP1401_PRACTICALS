def main():
    user_details = {}
    email = input("Enter email: ")

    # while loop
    while email != "":
        name = name_from_email(email)
        confirm_name = input("Is your name {}? (Y/N) ".format(name))
        if confirm_name.upper() != "Y" and confirm_name != "":
            name = input("Enter name: ")
        user_details[email] = name
        email = input("Enter Email: ")

    for email, name in user_details.items():
        print("{} ({})".format(name, email))


# remove @ and other characters in email to output just the name
def name_from_email(email):
    at_character = email.split('@')[0]
    special_characters = at_character.split('.')
    name = " ".join(special_characters).title()
    return name


main()
