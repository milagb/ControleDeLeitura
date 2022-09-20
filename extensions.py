from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#instanciar os dois objetos
db = SQLAlchemy()
migrate = Migrate()