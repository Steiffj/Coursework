def main():
    # Basic variables
    var = 12
    var += var
    print(var)
    var **= 2
    print(var)
    print("Type of 'var': ", type(var))

    income = 1000
    tax_rate = 0.12
    taxes = income * tax_rate
    print("Taxes: ", taxes)

    # Strings
    string = "Some string... it's useful"
    print(string[0] + string[-1] + string[len(string) - 1])
    print("Length is ", len(string))

main()
