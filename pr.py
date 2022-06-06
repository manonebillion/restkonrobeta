from database import *

class pr(BaseModel):
    idpr = PrimaryKeyField(null=False)
    kodepr = TextField()
    kodekelompok = TextField()
    pekan = TextField()
    entryby = IntegerField()
    dateentry = TextField()
    detail = TextField()
    lampiran = IntegerField()
    username = TextField()
    dateentrysql = IntegerField()
    entryfrom = TextField()

    @property
    def serialize(self):
        data = {
            'idpr': self.idpr,
            'kodepr': str(self.kodepr).strip(),
            'kodekelompok': str(self.kodekelompok).strip(),
            'pekan': str(self.pekan).strip(),
            'entryby': str(self.entryby).strip(),
            'dateentry': str(self.dateentry).strip(),
            'detail': str(self.detail).strip(),
            'lampiran': str(self.lampiran).strip(),
            'username': str(self.username).strip(),
            'dateentrysql': str(self.dateentrysql).strip(),
            'entryfrom': str(self.entryfrom).strip()
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.idpr,
            self.kodepr,
            self.kodekelompok,
            self.pekan,
            self.entryby,
            self.dateentry,
            self.detail,
            self.lampiran,
            self.username,
            self.dateentrysql,
            self.entryfrom
        )