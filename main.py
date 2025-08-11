from modules.balance import Balance
from modules.users import Customer, AdminUser, RegularUser
from modules.cli_colors import COLORS
import sys


# CLI Colors
GREEN = COLORS.GREEN
RED = COLORS.RED
RESET = COLORS.RESET


line_sep = str(f"####" + f"{GREEN}-{RESET}" * 40 + "####")


def login_menu():
    while True:
        try:
            print(line_sep)
            print(f"{GREEN}Welcome to our DEPI Shop!{RESET}")
            print(line_sep)
            print(f"{RED}1. Login\n2. Sign up\n3. Exit{RESET}")
            log_choice = int(input("Enter your choice: "))
            print(line_sep)

            if log_choice not in [1, 2, 3]:
                print(f"{RED}Invalid choice! Please choose 1, 2 or 3{RESET}")
                continue

            if log_choice == 3:
                print(f"{GREEN}Thank you for using DEPI Shop!{RESET}")
                sys.exit(0)

            customer = Customer()

            if log_choice == 1:
                return customer.login()
            elif log_choice == 2:
                new_id = customer.sign_up()
                print(f"{GREEN}Your ID is: {new_id}{RESET}")
                return customer.login()

        except ValueError:
            print(f"{RED}Please enter a valid number!{RESET}")
        except Exception as e:
            print(f"{RED}An error occurred: {str(e)}{RESET}")


def main():
    user = login_menu()
    while user:
        try:
            user.show_menu()
            choice = int(input("Enter your choice: "))

            if isinstance(user, AdminUser):
                if not 1 <= choice <= 7:
                    print(f"{RED}Invalid choice! Please choose 1-7{RESET}")
                    continue

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
                    user = login_menu()
            else:
                if not 1 <= choice <= 3:
                    print(f"{RED}Invalid choice! Please choose 1-3{RESET}")
                    continue

                if choice == 1:
                    user.inventory.show_products()
                elif choice == 2:
                    user.buy_product()
                elif choice == 3:
                    user = login_menu()

        except ValueError:
            print(f"{RED}Please enter a valid number!{RESET}")
        except Exception as e:
            print(f"{RED}An error occurred: {str(e)}{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Thank you for using DEPI Shop!{RESET}")
