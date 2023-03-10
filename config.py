import connexion
from flask_alembic import Alembic
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

connex_app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')

app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/data_telemetry'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

ma = Marshmallow(app)
db = SQLAlchemy(app)
alembic = Alembic(app)


