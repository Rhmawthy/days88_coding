#program mengurutkan kata 
h = input("masukkan satu kalimat  : ")

kata = h.split()
kata.sort()

for i in kata :
	print(i)