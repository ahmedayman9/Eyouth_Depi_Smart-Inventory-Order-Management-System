from modules import balance, customer, inventory, cli_colors

# CLI Colors
GREEN = cli_colors.COLORS.GREEN
RED = cli_colors.COLORS.RED
RESET = cli_colors.COLORS.RESET


line_sep = str(f"{GREEN}-{RESET}" * 40)

if __name__ == "__main__":
    print(line_sep)
    print(f"{GREEN}Welcome to our DEPI Shop!{RESET}")
    print(line_sep)
    print(f"{RED}1.login.\n2.sign up.{RESET}")
    log_choice = int(input("Enter your choice: "))
    print(line_sep)

    curr_customer = customer.Customer()
    if log_choice == 1:
        curr_customer.login()
    elif log_choice == 2:
        new_id = curr_customer.sign_up()
        print(f"Your Id is : {new_id}")

    while True:
        pass
        # todo
