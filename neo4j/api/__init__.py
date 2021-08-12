from flask_restful import Api

from neo4j.api.person.person_service import PersonService, PersonListService
from neo4j.api.movie.movie_service import MovieService, MovieListService
from neo4j.api.relation.relation_service import RelationService


api = Api(prefix='/api')

api.add_resource(PersonService, '/persons/<string:name>', endpoint='person')
api.add_resource(PersonListService, '/persons', endpoint='persons')

api.add_resource(MovieService, '/movies/<string:name>', endpoint='movie')
api.add_resource(MovieListService, '/movies', endpoint='movies')

api.add_resource(RelationService, '/person/<string:name>/rate', endpoint='relate')