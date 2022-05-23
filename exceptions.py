class LengthError(Exception):
    def __init__(self, message='Length Error'):
        super(LengthError, self).__init__(message)


class RecursionError(Exception):
    def __init__(self, message='Recursion Error'):
        super(RecursionError, self).__init__(message)    


class NameErrorCustom(Exception):
    def __init__(self, message='Name Error'):
        super(NameErrorCustom, self).__init__(message)

