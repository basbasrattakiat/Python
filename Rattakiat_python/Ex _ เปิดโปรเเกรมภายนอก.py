import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Word\n 2.Open PowerPoint\n 3.Exit')
    choice = input('Select Menu :')

def openpoint():
    filename = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"'
    print('powerpoint %s' %filename)
    os.system(filename)

def openword():
    filename = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
    print('word %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice == '1' :
        openword()
    elif choice == '2' :
        openpoint()
    else :
        break

'''import os
choice = 0
filename = ''

print("Welcome!! IAM48 Shop\n")
def menu():
    global choice
    print ("Menu\n  1.แสดงรายการสินค้า\n  2.หยิบสินค้าเข้าตะกร้า\n  3.แสดงรายการสินค้าในตะกร้าเเละรายการสินค้าที่หยิบ\n  4.ปิดโปรเเกรม\n")
    choice = input('Select Menu : ')

def liststore():
    store1 = ["1.BNK48 Single 5 : 200", "\n2.BNK48 Single 6 : 250", "\n3.BNK48 Single 7 : 300", "4.\nBNK48 Single 8 : 320", "5.\nCGM48 Single 1 : 350" ]
    print (store1)

def importstore():
    i = 1
    storelist = []
    print("กรอกรหัสสินค้า")
    while(i) :
        menu = input ("กรอกหมายเลขของสินค้า\t หากสินสุดรายการให้พิมพ์ 0 \t : ")
        i += 1
        if menu== "0" :
            break
        storelist.append (menu)

def showlist():
    print(storelist)
    print("SHOW....")

def exit():
    print("EXIT....")

while True:
    menu()
    if choice == '1' :
        liststore()
    elif choice == '2' :
        importstore()
    elif choice == '3' :
        showlist()
    elif choice == '4' :
        exit()
    else :
        exit()
        break'''