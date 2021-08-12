from flask.json import jsonify

from flask_restful import abort, reqparse, Resource

from neo4j.api.models.movie import Movie
from .movie_repository import MovieRepository


class MovieListService(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.repository = MovieRepository()

    def get(self):
        movies = self.repository.list()
        return jsonify([m.to_dict() for m in movies.all()])

    def post(self):
        self.parser.add_argument('name')

        args = self.parser.parse_args()

        new_movie = Movie(**args)
        self.repository.save(new_movie)
        return jsonify(new_movie.to_dict())


class MovieService(Resource):
    def __init__(self):
        self.repository = MovieRepository()

    def get(self, name):
        movie = self.repository.search(name)
        if movie is None:
            abort(404, message='Movie not found!')

        return jsonify(movie.to_dict())