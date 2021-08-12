from py2neo.ogm import GraphObject, Property, RelatedTo

class Person(GraphObject):
    __primarykey__ = "name"
    __primarylabel__ = "PERSON"

    name = Property()
    surname = Property()
    age = Property()
    country = Property()

    related = RelatedTo("neo4j.models.movie.Movie", 'HAS_RELATED')

    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "country": self.country
        }