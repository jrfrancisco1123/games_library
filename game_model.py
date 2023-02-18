from mysqlconnection import connectToMySQL

class Game:
    db = "gaming"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.console = data['console']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO games (name, console, genre, created_at, updated_at) VALUES (%(name)s, %(console)s, %(genre)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * From games;"
        results = connectToMySQL(cls.db).query_db(query)
        games = []
        for game in results:
            games.append(cls(game))
        return games

    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM games WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        return cls(results[0])

    @classmethod
    def update_game(cls, data):
        query = "UPDATE games SET name = %(name)s, console = %(console)s , genre = %(genre)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM games WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, {'id': id})