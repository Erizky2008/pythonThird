
class Mahasiswa(object):
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
    def getNim(self):
        return self.nim
    def setNim(self, nim):
        self.nim = nim
    def getNama(self):
        return  self.nama
    def setNama(self, nama):
        self.nama = nama
    def getAll(self):
        data = {
            'nim' : '12345',
            'nama' : 'tyaya',
            }
        return data