from flask_restful import Resource
from models.reader import Reader

class Race(Resource):
    def get(self):
        reader = Reader()
        return reader.logReader()