"""print("โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์\n")
print ("\tรถยนต์ 4 ล้อ\tกด 1\n\tรถยนต์ 6 ล้อ\tกด 2\n\tรถยนต์มากกว่า 6 ล้อ \t กด 3")

car = input("เลือกประเภทรถยานพาหนะ : ")
car1 = ["ลาดกระบัง ไป บางบ่อ : 30", "ลาดกระบัง ไป บางประกง : 45", "ลาดกระบัง ไป พนัสนิคม : 55", "ลาดกระบัง ไป บ้านบึง : 60", "ลาดกระบัง ไป บางพระ : 80" ]
car2 = ["ลาดกระบัง ไป บางบ่อ : 30", "ลาดกระบัง ไป บางประกง : 45", "ลาดกระบัง ไป พนัสนิคม : 55", "ลาดกระบัง ไป บ้านบึง : 60", "ลาดกระบัง ไป บางพระ : 80" ]
car3 = ["ลาดกระบัง ไป บางบ่อ : 30", "ลาดกระบัง ไป บางประกง : 45", "ลาดกระบัง ไป พนัสนิคม : 55", "ลาดกระบัง ไป บ้านบึง : 60", "ลาดกระบัง ไป บางพระ : 80" ]
x = car1
print(x)"""

"""x = input("กด 1 เลือกเหมาจ่าย\t กด 2 เลือกจ่ายเพิ่ม\n")
km = input("ระยะทาง กิโลเมตร")
print (x)
if x == 1:
    if km <= 25:
       print("ค่าใช้จ่ายทั้งหมด 25 บาท")
    else:
       print("ค่าใช้จ่ายทั้งหมด 55 บาท")
elif x==2:
    if km < 25:
       print("ค่าใช้จ่ายทั้งหมด 25 บาท")
    else:
       print("ค่าใช้จ่ายทั้งหมด 55 บาท")"""

"""#22.01.2021 เเบบฝึกหัด 3.1
x = int (input("กด 1 เลือกเหมาจ่าย\t กด 2 เลือกจ่ายเพิ่ม\n")) #ตอนเเรกมันเข้ามาได้ เเต่อย่าลืมว่าต้องเเปลงเป็น int ด้วย ภาษามันไม่รู้ หรือเรางงเอา
if x==1: #ถ้า x = 1
    km = int (input("KM : ")) #เเปลงเป็น int ให้เครื่องด้วย มันไม่รู้อ่ะ 555
    print("SUM = 25") if km <= 25 else print("SUM = 55")
else : #ถ้า x = 2
    km = int (input("KM : "))  #เเปลงเป็น int ตอนเเรกที่มันไม่ได้ ไม่ได้เเปลงค่าในตัวเเปร (ความรู้ week1)
    print("SUM = 80") if km <= 25 else print("SUM = 25")
    # เปรียบเทียบ if else"""

"""#22.01.2021 เเบบฝึกหัด 3.2
i = 1
count = 0
n = int (input("กรุณากรอกตัวเลขจำนวนครั้งในการรับค่า \n"))
while(i <= n) :
    sum = int(input ("กรอกตัวเลข\t"))
    count = count+sum
    i += 1
print (count)"""


"""#22.01.2021 เเบบฝึกหัด 3.3 โปรเเกรมรายการอาหาร
i = 1
food = []
print("ป้อนชื่ออาหารสุดโปรดของตุณ หรือ ออกเพื่อออกจากโปรเเกรม")
while(i) :
    menu = input ("รายการอาหาร\t")
    i += 1
    if menu== "ออก" :
        break
    food.append (menu)
print ("รายการอาหารที่คุณชอบ ")
for x in range (1,i) :
    print (x,".",food[x-1])"""

"""#22.01.2021 เเบบฝึกหัด 3.4 โปรเเกรมร้านค้า
print ("ฐานข้อมูลนักเรียน")
print ("  เพิ่มรายชื่อ [a]\n  แสดงรายชื่อ [s]\n  ออกจากระบบ [x]\n")"""

"""food = []
print 
while(i) :
    menu = input ("รายการอาหาร\t")
    i += 1
    if menu== "exit" :
        break
    food.append (menu)
print (food)"""


#22.01.2021 เเบบฝึกหัด 3.4 โปรเเกรมร้านค้า
a=[]
while True:
    b = input('----ร้านคุณหลินบิวตี้----\n เพิ่ม, [a]\n แสดง [s]\n ออกจากโปรแกรม [x]\n')
    b = b.lower()
    if b== 'a' :
        c = input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's' :
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format("รหัส","ชื่อ","จังหวัด"))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a:
            e = d.split(":")
            print('{0[0]:<6}{0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x':
        break
    print('ทำคำสั่งถัดไป')