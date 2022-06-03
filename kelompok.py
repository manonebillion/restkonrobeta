from database import *

class kelompok(BaseModel):
    id = PrimaryKeyField(null=False)
    kodekelompok = TextField()
    email = TextField()
    tokensent = TextField()
    tokensentsql = IntegerField()
    status = TextField()
    respontime = TextField()
    responsql = IntegerField()
    lockmember = TextField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'kodekelompok': str(self.kodekelompok).strip(),
            'email': str(self.email).strip(),
            'tokensent': str(self.tokensent).strip(),
            'tokensentsql': str(self.tokensentsql).strip(),
            'status': str(self.status).strip(),
            'respontime': str(self.respontime).strip(),
            'responsql': str(self.responsql).strip(),
            'lockmember': str(self.lockmember).strip(),
            
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.id,
            self.kodekelompok,
            self.email,
            self.tokensent,
            self.tokensentsql,
            self.status,
            self.respontime,
            self.responsql,
            self.lockmember,
            
        )