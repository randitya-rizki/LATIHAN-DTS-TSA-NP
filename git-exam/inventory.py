file = open("db-inventory.txt", "a")
while True:
    data = input("Input Data Inventory baru (ya/tidak)?")
    print("***********************************")
    if data == "ya":
        x = input("Nama Perangkat: ")
        y = input("Lokasi: ")
        print("---------------------------------")
    else:
        file = open("db-inventory.txt","r")
        for item in file:
            print(item)
        file.close()  
        break
    file.write("Nama Perangkat: " + (x + ", ") +"Lokasi: " + y + "\n")
file.close()