"""
Usage:
    Run the script and type any command. The script will echo the command back.
    To exit the loop and terminate the script, type "quit".
"""

command = ""

while command.lower() != "quit":
    command = input("$ ")
    print(f"echo: {command}")
