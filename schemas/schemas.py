from flask_marshmallow.fields import fields

from config import ma
from models.entities import Data


class DataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")

    class Meta:
        model = Data
        load_instance = True
        exclude = ["data_id"]
