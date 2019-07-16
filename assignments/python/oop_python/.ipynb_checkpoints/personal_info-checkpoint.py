from collections import namedtuple
from functools import reduce

personal_details = namedtuple('personal_details','date_of_birth')
personal_features = namedtuple('personal_features', 'eye_color iq_score')

person_1_details = personal_details(date_of_birth='09-04-1991')
person_1_features = personal_features(eye_color='Green', iq_score=109)


class PersonalJoiner:
    @staticmethod
    def join(*args):
        keys = []
        values = []

        for i in args:
            olist = i._asdict()
            i_keys = [key for key in olist.keys()]
            keys = keys + i_keys

            i_vals = [val for val in olist.values()]
            values = values + i_vals

        key_vals = dict(zip(keys, values))

        Person = namedtuple('Person', keys)
        person = Person(**key_vals)

        return person






