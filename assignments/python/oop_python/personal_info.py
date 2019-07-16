from collections import namedtuple


class PersonalJoiner:
    @staticmethod
    def join(*args):
        all_attributes = {}

        for i in args:
            all_attributes.update(i._asdict())

        Person = namedtuple('Person', all_attributes.keys())
        person = Person(**all_attributes)

        return person
