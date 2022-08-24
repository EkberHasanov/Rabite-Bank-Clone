from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/RabiteBank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "SECRET_KEY"


from extensions import db, migrate
from controllers import *
# from controls import *
from models import *


if __name__ == "__main__":
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1:3306/first'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# from controls import *

# if(__name__ == '__main__'):
#     app.run(port = 5000,debug = True)
