# python errors and exceptions
#   exceptions hierarchy: https://profound.academy/python-mid/exception-hierarchy-phonbKOpXJ362GhumAsG

def division(num_01, num_02):
    if num_02 == 0:
        raise ZeroDivisionError(
            "Can not divide by 0",
            {"num_01": num_01, "num_02": num_02}
        )
    return num_01 / num_02


try:
    division(100, 0)
except Exception as e:
    print(e)

# OUTPUT
# Can not divide by 0
