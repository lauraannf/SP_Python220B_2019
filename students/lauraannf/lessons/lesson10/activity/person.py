# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:36:55 2019

@author: Laura.Fiorentino
"""


class Person:
    def __init__(self, first_name="", last_name="", phone=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        msg = ["Person:"]
        for name, val in vars(self).items():
            msg.append("{}: {}".format(name, val))
            return "\n".join(msg)


def update_person(person):
    while True:
        att = input("What would you like to update for :\n"
                    "{}\n"
                    '(type "quit" to quit) >> '.format(person))
        if att.strip().lower() == "quit":
            break
        if not hasattr(person, att):
            ans = input("This person does not have that attribute.\n"
                        "Would you like to add it? Y or N>> ")
            if not ans.lower().startswith('y'):
                continue
        ans = input("What would you like to set it to?>> ")
        setattr(person, att, ans)


if __name__ == "__main__":
    p1 = Person("Fred", "Jones", "1")
    update_person(p1)
