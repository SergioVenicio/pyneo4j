from py2neo.ogm import Repository


class BaseRepository:
    def __init__(self):
        self.graph = Repository(f'bolt://neo4j@localhost:7687', password='s3cr3t')

    def save(self, node):
        self.graph.merge(node)

    def push(self, node):
        self.graph.push(node)