from flask.json import jsonify

from flask_restful import abort, reqparse, Resource

from neo4j.api.models.person import Person
from .person_repository import PersonRepository


class PersonListService(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.repository = PersonRepository()

    def get(self):
        persons = self.repository.list()
        return jsonify([p.to_dict() for p in persons.all()])

    def post(self):
        self.parser.add_argument('name')
        self.parser.add_argument('surname')
        self.parser.add_argument('age')
        self.parser.add_argument('country')

        args = self.parser.parse_args()

        new_person = Person(**args)
        self.repository.save(new_person)
        return jsonify(new_person.to_dict())


class PersonService(Resource):
    def __init__(self):
        self.repository = PersonRepository()

    def get(self, name):
        person = self.repository.search(name)
        if person is None:
            abort(404, message='Person not found!')

        return jsonify(person.to_dict())