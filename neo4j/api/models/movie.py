from py2neo.ogm import GraphObject, Property, RelatedTo


class Movie(GraphObject):
    __primarykey__ = "name"
    __primarylabel__ = "MOVIE"

    name = Property()

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name
        }