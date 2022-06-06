from database import *

class user(BaseModel):
    id = PrimaryKeyField(null=False)
    username = TextField()
    password = TextField()
    level_akses = TextField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'username': str(self.username).strip(),
            'password': str(self.password).strip(),
            'level_akses': str(self.level_akses).strip()
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}".format(
            self.id,
            self.username,
            self.password,
            self.level_akses
        )