import csv

def check_type(user_name, password):
    with open(r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\users.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        user_found = False
        for row in reader:
            if row["user_name"] == user_name:
                user_found = True
                if row["Password"] == password:
                    print("Login Successfully")
                    return row["Type"]
                else:
                    print("Password wrong! Try again.")
                    return False

        if not user_found:
            print("User name doesn't exist!")
            return False