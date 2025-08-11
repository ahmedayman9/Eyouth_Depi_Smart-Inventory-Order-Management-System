from modules.balance import Balance
from modules.users import Customer, AdminUser, RegularUser
from modules.cli_colors import COLORS


# CLI Colors
GREEN = COLORS.GREEN
RED = COLORS.RED
RESET = COLORS.RESET


line_sep = str(f"####" + f"{GREEN}-{RESET}" * 40 + "####")

if __name__ == "__main__":
    print(line_sep)
    print(f"{GREEN}Welcome to our DEPI Shop!{RESET}")
    print(line_sep)
    print(f"{RED}1.login.\n2.sign up.{RESET}")
    log_choice = int(input("Enter your choice: "))
    print(line_sep)

    customer = Customer()
    user = None

    if log_choice == 1:
        user = customer.login()
    elif log_choice == 2:
        new_id = customer.sign_up()
        print(f"Your Id is : {new_id}")
        user = customer.login()

    while user:
        user.show_menu()
        choice = int(input("Enter your choice: "))

        if isinstance(user, AdminUser):
            if choice == 1:
                user.inventory.show_products()
            elif choice == 2:
                user.add_product()
            elif choice == 3:
                user.update_product()
            elif choice == 4:
                user.show_profit()
            elif choice == 5:
                user.view_users()
            elif choice == 6:
                ch = user.balance.show_menu()
                user.balance.show_sales(ch)
            elif choice == 7:
                break
        else:
            if choice == 1:
                user.inventory.show_products()
            elif choice == 2:
                user.buy_product()
            elif choice == 3:
                break
