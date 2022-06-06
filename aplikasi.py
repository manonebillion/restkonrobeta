from database import *

class aplikasi(BaseModel):
    idaplikasi = PrimaryKeyField(null=False)
    namaaplikasi = TextField()
    deskripsi = TextField()
    url_konro = TextField()
    poster = TextField()
    presentasi = TextField()
    laporan = TextField()
    kodekelompok = TextField()
    url_repo = TextField()
    anyar = TextField()
    openstat = TextField()
    anyarppt = TextField()
    anyardoc = TextField()
    nilaiangka = TextField()
    nilaihuruf = TextField()
    nilaiangkaUAS = TextField()
    nilaihurufUAS = TextField()

    @property
    def serialize(self):
        data = {
            'idaplikasi': self.idaplikasi,
            'namaaplikasi': str(self.namaaplikasi).strip(),
            'deskripsi': str(self.deskripsi).strip(),
            'url_konro': str(self.url_konro).strip(),
            'poster': str(self.poster).strip(),
            'presentasi': str(self.presentasi).strip(),
            'laporan': str(self.laporan).strip(),
            'kodekelompok': str(self.kodekelompok).strip(),
            'url_repo': str(self.url_repo).strip(),
            'anyar': str(self.anyar).strip(),
            'openstat': str(self.openstat).strip(),
            'anyarppt': str(self.anyarppt).strip(),
            'anyardoc': str(self.anyardoc).strip(),
            'nilaiangka': str(self.nilaiangka).strip(),
            'nilaihuruf': str(self.nilaihuruf).strip(),
            'nilaiangkaUAS': str(self.nilaiangkaUAS).strip(),
            'nilaihurufUAS': str(self.nilaihurufUAS).strip()
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {},{}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}".format(
            self.idaplikasi,
            self.namaaplikasi,
            self.deskripsi,
            self.url_konro,
            self.poster,
            self.presentasi,
            self.laporan,
            self.kodekelompok,
            self.url_repo,
            self.anyar,
            self.openstat,
            self.anyarppt,
            self.anyardoc,
            self.nilaiangka,
            self.nilaihuruf,
            self.nilaiangkaUAS,
            self.nilaihurufUAS
        )