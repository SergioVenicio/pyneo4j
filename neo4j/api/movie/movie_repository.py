from ..base_repository import BaseRepository

from neo4j.api.models import movie


class MovieRepository(BaseRepository):
    def list(self):
        return self.graph.match(movie.Movie)

    def search(self, name):
        return self.graph.match(movie.Movie).where(name=name).first()