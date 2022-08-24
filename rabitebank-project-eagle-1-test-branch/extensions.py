from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app)

from models import Category, News, Companies

admin.add_view(ModelView(News, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Companies, db.session))