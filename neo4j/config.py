import os

from dotenv import load_dotenv


load_dotenv()


class DefaultConfig:
    DEBUG = os.getenv('DEBUG', False)
    NEO4J_HOST = os.getenv('NEO4J_HOST', False)
    NEO4J_PORT = os.getenv('NEO4J_PORT', 7687)
    NEO4J_USER= os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PWD= os.getenv('NEO4J_PWD', 's3cr3t')