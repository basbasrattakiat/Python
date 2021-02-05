import os
choice = 0
listIAM = [0,0,0,0,0]
pick = 0

def menu():
    global choice
    print('Menu\n  1.แสดงรายการสินค้า\n  2.เลือกสินค้าเข้า\n  3.แสดงจำนวนรายการเเละราคาสินค้า\n  4.นำสินค้าออก\n  5.ปิดการทำงานของโปรแกรม')
    choice = input('เลือกรายการที่ต้องการ :')
    screen_clear()

def show_item():
    print("\t\n รายการสินค้า\n  1. PhotoBook ราคา 350 บาท\n  2.PhotoSet ราคา 250 บาท\n  3.CD ราคา 350 บาท\n  4.Ticket ราคา 1000 บาท\n  5.MusicCard ราคา 200 บาท\n")

def export_item():
    global pick
    print("\t\n รายการสินค้า\n  1. PhotoBook ราคา 350 บาท\n  2.PhotoSet ราคา 250 บาท\n  3.CD ราคา 350 บาท\n  4.Ticket ราคา 1000 บาท\n  5.MusicCard ราคา 200 บาท\n")
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listIAM[0] -= 1
    elif depick == 2:
        listIAM[1] -= 1
    elif depick == 3:
        listIAM[2] -= 1
    elif depick == 4:
        listIAM[3] -= 1
    elif depick == 5:
        listIAM[4] -= 1
    screen_clear()

def showlist():
    list_item = ['PhotoBook','PhotoSet','CD','Ticket','MusicCard']
    list_price = [350,250,350,1000,100]

def pickmenu():
    global pick
    print("\t\n รายการสินค้า\n  1. PhotoBook ราคา 350 บาท\n  2.PhotoSet ราคา 250 บาท\n  3.CD ราคา 350 บาท\n  4.Ticket ราคา 1000 บาท\n  5.MusicCard ราคา 200 บาท\n")
    pick = int(input('เลือกสินค้าหมายเลข :   '))
    if pick == 1:
        listIAM[0] += 1
    elif pick == 2:
        listIAM[1] += 1
    elif pick == 3:
        listIAM[2] += 1
    elif pick == 4:
        listIAM[3] += 1
    elif pick == 5:
        listIAM[4] += 1
    screen_clear()

def screen_clear():
    import os
    os.system('cls')

while(True) :
    menu()
    if choice == '1':
        screen_clear()
        show_item()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showlist()
    elif choice == '4':
        screen_clear()
        export_item()
    elif choice == '5':
        c= input('ต้องการใช้งานโปรเเกรมต่อหรือไม่ Y/N: ')
        if c.lower() == 'Y' :
            screen_clear()
        elif  c.lower() == 'N' :
            screen_clear()
            break