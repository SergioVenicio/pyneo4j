from flask.json import jsonify

from flask_restful import abort, reqparse, Resource

from neo4j.api.movie.movie_repository import MovieRepository
from neo4j.api.person.person_repository import PersonRepository


class RelationService(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.person_repository = PersonRepository()
        self.movie_repository = MovieRepository()

    def post(self, name):
        self.parser.add_argument('movie_name')

        args = self.parser.parse_args()

        person = self.person_repository.search(name)
        if person is None:
            abort(400, message='Person not found!')

        movie = self.movie_repository.search(args['movie_name'])
        if movie is None:
            abort(400, message='Movie not found!')

        person.related.add(movie, stars=5)
        self.person_repository.push(person)
            
        return jsonify({'message': 'Ok'})
