def math_divide(n1, n2):
    try:
        result = n1 / n2

    except ZeroDivisionError:
        # when zerodivisionerror happens
        print("you cannot divide by zero")

    else:
        # when no errors happen
        print("Division was successful")

    finally:
        # no error or error - runs last
        print("Operation done")


math_divide(10, 5)
math_divide(20, 0)
