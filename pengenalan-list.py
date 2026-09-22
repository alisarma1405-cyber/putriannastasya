# contoh list 
list_1 = [10, 70, 20]

# list dengan deklarasi element secara vertikal 
list_2 = [ 'ab', 'cd', 'hi', 'ca' ]

# list dengan element berisi bermacam-macam tipe data 
list_3 = [3.14, 'hello python', True, False]

# list kosong 
list_4 = []

list_1 = [10, 70, 20]
for e in list_1: 
    print("elem:", e)
    
list_1 = [10, 70, 20] 
for i in range(0, len(list_1)): 
    print("index:", i, "elem:", list_1[i])