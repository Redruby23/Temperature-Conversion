def to_celsius(fahrenheit):
    celsius = (fahfenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# the main function is used to test the other functions


if _name_ == "_main_":
    for temp in range (0, 212, 40): 
        print(temp, "fahrenheit", round(to_celsius(temp), 2), "celsius")
    for temp in range(0, 101, 20):
        print(temp, "celsius =", round(to_fahrenheit(temp), 2),