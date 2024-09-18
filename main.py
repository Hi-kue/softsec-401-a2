from config.log_config import logger as log
from config import sqlite_config as sqlte

# rich imports
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

import os
import glob
import sys

console = Console()


def menu():
    menu_title = Text()
    menu_title.append("Simple Banking Application\n", style="bold gray")
    menu_title.append("[1] - Create User\n", style="bold gray")
    menu_title.append("[2] - Deposit\n", style="bold gray")
    menu_title.append("[3] - Withdraw\n", style="bold gray")
    menu_title.append("[4] - Check Balance\n", style="bold gray")
    menu_title.append("[5] - Exit or Quit (type 'exit', 'quit', or 'e')\n", style="red")

    menu_panel = Panel(
        menu_title,
        title="[bold white] Menu Options",
        expand=False,
        border_style="bold",
        padding=(2, 2),
    )

    console.print(menu_panel)


def run_db_setup():
    db_file = glob.glob(os.path.join("db", "*.db"))
    existing_db_route = None

    if db_file:
        existing_db_route = db_file[0]
        log.info(f"Existing Database File: {existing_db_route}")

        if len(db_file) > 1:
            log.warning("Multiple Database Files Found, Removing Extra Files...")
            for file in db_file[1:]:
                os.remove(file)

    sqlite_instance = sqlte.Sqlite.get_instance(existing_db_route)

    for row in sqlite_instance.execute_query("""SELECT * FROM user"""):
        log.info(row)

    sqlite_instance.__exit__(None, None, None)


def create_user():
    pass


def deposit_to_account():
    pass


def withdraw_from_account():
    pass


def check_balance_on_account():
    pass


if __name__ == "__main__":
    run_db_setup()

    user_answer = ""

    while user_answer.lower() not in ["exit", "quit", "e"]:
        menu()

        user_answer = input("Enter your choice: ")

        match user_answer.lower():
            case "1" | "cu" | "create user":
                break

            case "2" | "d" | "deposit":
                break

            case "3" | "w" | "withdraw":
                break

            case "4" | "cb" | "check balance":
                break

            case "exit" | "quit" | "e":
                log.info("Exiting Application...")
                sys.exit(0)

            case _:
                console.print("Invalid Option, Please Try Again", style="bold red")
                continue
