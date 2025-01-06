while True:
    message = """
        Welcome to my first calculator! :))
        write 'exit' to finish the program
    """
    print(message)

    number_one = input("Enter the first number: ")
    if number_one.lower() == "exit":
        break

    number_two = input("Enter the second number: ")
    if number_two.lower() == "exit":
        break

    operation = input("Operation: sum, rest, multi, div: ")
    while operation.lower() not in ["sum", "rest", "multi", "div", "exit"]:
        operation = input("Operation: sum, rest, multi, div: ")

    if operation.lower() == "exit":
        break

    number_one = int(number_one)
    number_two = int(number_two)
    result = 0

    if operation.lower() == "sum":
        result = number_one + number_two

    if operation.lower() == "rest":
        result = number_one - number_two

    if operation.lower() == "multi":
        result = number_one * number_two

    if operation.lower() == "div":
        result = number_one / number_two

    print(f"{number_one}, {number_two}. Result: {result}")
