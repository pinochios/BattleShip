class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


"""a = 10

while True:
    try:
        x = int(input())
        if x < a:
            pass
        else:
            raise ValueTooLargeError
    except ValueError:
        print("Invalid value, please try again")
    except ValueTooLargeError:
        print("Too large value, please try again")
    else:
        break
"""
