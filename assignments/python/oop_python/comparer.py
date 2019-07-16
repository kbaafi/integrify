class StringComparator(str):
    #def __new__(cls, base_string):
    #   print("Creating instance")
    #    instance = super(StringComparator, cls).__new__(cls, base_string)
    #    return instance

    def __init__(self, base_string=""):
        self.base_string = base_string.replace(' ', '')
        self.base_string

    def __le__(self, other):
        other_string = other.replace(' ', '')
        if len(self.base_string) <= len(other_string):
            return True
        return False

    def __ge__(self, other):
        other_string = other.replace(' ', '')
        if len(self.base_string) >= len(other_string):
            return True
        return False

    def __lt__(self, other):
        other_string = other.replace(' ', '')
        if len(self.base_string) < len(other_string):
            return True
        return False

    def __gt__(self, other):
        other_string = other.replace(' ', '')
        if len(self.base_string) > len(other_string):
            return True
        return False

    def __eq__(self, other):
        other_string = other.replace(' ', '')
        if len(self.base_string) == len(other_string):
            return True
        return False
