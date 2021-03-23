class MahasiswaView(object):
    def formMahasiswa(self):
        nim = int(input('masukkan nim : '))
        nama = input('masukkan nama : ')

        data = {
            'nim' : nim,
            'nama' : nama
        }
        return data
    def pilih(self):
        print("[1]. view : \n [2]. exit")
        option = input('Pilih ; ')
        return option
    def tampil(self, data):
        print('nim' + str(data['nim']))
        print('nama' + data['nama'])