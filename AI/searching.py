#Nama = Novita Fadilah Datuamas
#NIM = F55123002
x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

def heuristic_search(x, y1, y2):
    if y1 in x:
        return x.index(y1)  
    elif y2 in x:
        return 4  # Mengembalikan 4 jika y2 ditemukan
    else:
        return 0  # Mengembalikan 0 jika y1 dan y2 tidak ditemukan

output = heuristic_search(x, y1, y2)
print("Output:", output)