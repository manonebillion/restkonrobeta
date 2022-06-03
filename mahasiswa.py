from database import *

class mahasiswa(BaseModel):
    idmahasiswa = PrimaryKeyField(null=False)
    nim = TextField()
    nama = TextField()
    kelas = TextField()
    email = TextField()
    hp = TextField()
    hptelegram = TextField()
    keterangan = TextField()
    username = TextField()
    kodekelompok = TextField()
    nilaiangka = TextField()
    nilaihuruf = TextField()
    chatid = TextField()
    nilaiangkaUAS = TextField()
    nilaihurufUAS = TextField()
    idtelegram = TextField()

    @property
    def serialize(self):
        data = {
            'idmahasiswa': self.idmahasiswa,
            'nim': str(self.nim).strip(),
            'nama': str(self.nama).strip(),
            'kelas': str(self.kelas).strip(),
            'email': str(self.email).strip(),
            'hp': str(self.hp).strip(),
            'hptelegram': str(self.hptelegram).strip(),
            'keterangan': str(self.keterangan).strip(),
            'username': str(self.username).strip(),
            'kodekelompok': str(self.kodekelompok).strip(),
            'nilaiangka': str(self.nilaiangka).strip(),
            'nilaihuruf': str(self.nilaihuruf).strip(),
            'chatid': str(self.chatid).strip(),
            'nilaiangkaUAS': str(self.nilaiangkaUAS).strip(),
            'nilaihurufUAS': str(self.nilaihurufUAS).strip(),
            'idtelegram': str(self.idtelegram).strip()
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            self.idmahasiswa,
            self.nim,
            self.nama,
            self.kelas,
            self.email,
            self.hp,
            self.hptelegram,
            self.keterangan,
            self.username,
            self.kodekelompok,
            self.nilaiangka,
            self.nilaihuruf,
            self.chatid,
            self.nilaiangkaUAS,
            self.nilaihurufUAS,
            self.idtelegram
        )