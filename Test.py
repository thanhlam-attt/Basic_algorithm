n = int(input("Nhập n: "))


def Phantich_Nhiphan(n):
    So_Nhiphan = []
    while n > 0:
        sodu = n % 2
        n = n // 2
        So_Nhiphan.append(sodu)
    So_Nhiphan.reverse()
    return So_Nhiphan


K = Phantich_Nhiphan(n)
# K.reverse()
print(K)
