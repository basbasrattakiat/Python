word = {}
def menu():
    print('พจนานุกรม')
    print('1. เพิ่มคำศัพท์')
    print('2. แสดงคำศัพท์')
    print('3. ลบคำศัพท์')
    print('4. ปิดโปรเเกรม')

def add(): #เพิ่มคำศัพท์
    a = input ('เพิ่มคำศัพท์  :  ')
    b = input ('ชนิดคำศัพท์ (n.,v.,adj.,adv.)  :  ')
    c = input ('ความหมาย  :  ')
    word.update({a:{b,c}})
    screen_clear()

def view(): #แสดงคำศัพท์
    screen_clear()
    print('-'*50)
    print(' '*18 + "คำศัพท์ของคุณมีดังนี้"+' '*18)
    print(' '*50)
    print('{0:-<15}{1:-<15}{2:-<10}'.format('คำศัพท์','ชนิดศัพท์','ความหมาย'))
    for x,z in word.items():
        print(x+'\t',z)

def remove(): #ลบคำศัพท์
    q = input('พิมพ์คำตอบที่ต้องการลบ  :  ')                  
    yesno = input('ยืนยันการลบคำศัพท์ใช่หรือไม่ (y/n) :  ')     
    if yesno == 'y' :                                     
        word.pop(q)                                       
    else:
        print(' ')
    screen_clear()

def screen_clear():
    import os
    os.system('cls')                     

while True:
    menu()
    ch = int(input ('เลือกรายการ  :  '))
    if ch == 1:
        add()
    elif ch == 2:
        view()
    elif ch == 3:
        remove()
    elif ch == 4:
        yesno = input('ยืนยันการออกจากโปรเเกรมใช่หรือไม่ (y/n) :  ')
        if yesno == 'y' :
            screen_clear()
            break
        else:
            print('')
    else:
        print('')