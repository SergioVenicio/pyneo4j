from ..base_repository import BaseRepository

from neo4j.api.models import person


class PersonRepository(BaseRepository):
    def list(self):
        return self.graph.match(person.Person)

    def search(self, name):
        return self.graph.match(person.Person).where(name=name).first()