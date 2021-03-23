# score sebagai var | array |list
# mie = ['rendang', 'original', 'pedas']
# search = 'original'
# find = False

#looping
# for a in range(len(mie)):
#     if mie[a] == search:
#         print(f'data ditemukan : {search}')
#         find = True
#         break
#     else:
#         print('tidak ditemukan\n', search)
    # print(a)

# function
def mie():
    mie = ['rendang', 'original', 'pedas']
    search = input('cari mie : ')
    find = False
    for a in range(len(mie)):
        if mie[a] == search:
            print(f'data ditemukan : {search}')
            find = True
    else:
        print('tidak ditemukan')
    return find, search
print(mie())
