from database import *

class rating(BaseModel):
    id = PrimaryKeyField(null=False)
    rating = TextField()
    idaplikasi = TextField()
    idmahasiswa = TextField()
    waktu = TextField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'rating': str(self.rating).strip(),
            'idaplikasi': str(self.idaplikasi).strip(),
            'idmahasiswa': str(self.idmahasiswa).strip(),
            'waktu': str(self.waktu).strip()
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(
            self.id,
            self.rating,
            self.idaplikasi,
            self.idmahasiswa,
            self.waktu
        )