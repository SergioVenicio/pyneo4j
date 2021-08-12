from neo4j import create_app


app = create_app()

if __name__ == '__main__':
    app.run()
