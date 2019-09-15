from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.store import StoreList,Store
from resources.user import UserRegister
from resources.item import Item,ItemList

app = Flask(__name__)
app.secret_key = 'jose'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nawaz123@localhost/Cowork_PV'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate,identity) #/auth


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,"/register")
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=10000,debug=True)