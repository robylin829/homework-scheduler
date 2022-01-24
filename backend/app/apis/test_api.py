from flask_restx import Resource, Namespace 

test = Namespace('test', description='Test')

@test.route('/')
class Test(Resource):
    def get(self):
        return {"Hello": "World"}