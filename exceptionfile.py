class String_Exception(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __repr__(self):
        return self.message

class Integer_Exception(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __repr__(self):
        return self.message

class Range_Exception(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __repr__(self):
        return self.message