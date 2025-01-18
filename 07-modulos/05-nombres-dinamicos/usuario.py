
# if you run this file directly you will see the name name
# as "__main__". Because is the main context.

print(f"name in usuario.py is: {__name__}")

if __name__ != "__main__":
    from bank import notifier

    def pay_tax(money):
        print(f"is paying {money}")
        notifier()


# OUTPUT when you run this code directly.
# __main__
# is paying 64
