from model import Mahasiswa
from view import MahasiswaView


class MahasiswaController(object):
    def createMahasiswa(self):
        view = MahasiswaView()
        data = view.formMahasiswa()

        return data

    def tampilan(self, data):
        view = MahasiswaView()
        option = view.pilih()

        if option == '1':
            self.tampilMahasiswa(data)
        elif option == '2':
            print('stop')
        else:
            print('gak nemu')

    def tampilMahasiswa(self, data):
        view = MahasiswaView()
        view.tampil(data)

        self.tampilan(data)

    def run(self):
        registrasi = self.createMahasiswa()
        nim = registrasi['nim']
        nama = registrasi['nama']

        data = Mahasiswa(nim, nama)

        dataMahasiswa = data.getAll()
        self.tampilan(dataMahasiswa)

