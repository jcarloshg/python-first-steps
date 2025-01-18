try:
    int(input("Ingresa un número: "))
except Exception as e:
    print(f"Error: {e}")
else:
    print("There has not been an error")
finally:
    print("In the block finally")

# OUTPUT ERROR
# Ingresa un número: asd
# Error: invalid literal for int() with base 10: 'asd'
# In the block finally

# OUTPUT SUCCESS
# Ingresa un número: 123
# There has not been an error
# In the block finally
