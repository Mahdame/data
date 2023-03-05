import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config import db


class Data(db.Model):
    __tablename__ = "data"

    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, unique=False)

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle, date_time):
        self.data_id = data_id
        self.vehicle = vehicle
        self.date_time = date_time

    def __repr__(self):
        return 'Data(data_id=%d, vehicle=%s, date_time=%s)' % (
            self.data_id, self.vehicle, self.date_time)

    def json(self):
        return {'data_id': str(self.data_id), 'vehicle': self.vehicle, 'date_time': self.date_time}
