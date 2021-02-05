# นายรัฐเกียรติ หริ่มเพ็ง รหัสนักศึกษา 633050137-2
# แบบฝึกหัดที่ 4.1 
shop_list=[]
amount=[0,0,0,0,0]
price=[250,200,380,380,144]

def out_item():
    n=0
    while(True):
        print("\tสินค้าในตะกร้ามีดังนี้")
        for i in shop_list:
            n+=1
            print("\t"+str(n)+"."+i)
        n=0
        c=int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก : "))
        try:
            if c<=len(shop_list) and c!=-1:
                shop_list.pop(c-1)
            elif c==0 and c<=len(shop_list) and c!=-1:
                shop_list.pop(c)
            elif c==-1:
                break
        except:
            print("กรุณากรอกลำดับสินค้าให้ถูกต้อง")

def list_item():
    print("\tรายการสินค้า")
    print("------------------------------")
    print("\t1.BNK48 Photoset Shonichi : 250 BATH")
    print("\t2.BNK48 BADGE MERRY X'MAS : 200 BATH")
    print("\t3.BNK48 9th Single Senbatsu General Election Book : 380 BATH")
    print("\t4.CGM48 Towel : 380 BATH")
    print("\t5.BNK48 Belt Wristband : 2nd Generation The Debut : 144 BATH")

def pick_item():
    c=0
    while(True):
        print("\t1.BNK48 Photoset Shonichi")
        print("\t2.BNK48 BADGE MERRY X'MAS")
        print("\t3.BNK48 9th Single Senbatsu General Election Book")
        print("\t4.CGM48 Towel")
        print("\t5.BNK48 Belt Wristband : 2nd Generation The Debut")
        c=(input("เลือกสินค้าหมายเลข : "))
        try:
            if int(c)==1 or c=="1":
                shop_list.append("BNK48 Photoset Shonichi")
            elif int(c)==1 or c=="21":
                shop_list.append("BNK48 BADGE MERRY X'MAS")
            elif int(c)==1 or c=="3":
                shop_list.append("BNK48 9th Single Senbatsu General Election Book")
            elif int(c)==1 or c=="4":
                shop_list.append("CGM48 Towel")
            elif int(c)==1 or c=="5":
                shop_list.append("BNK48 Belt Wristband : 2nd Generation The Debut")
            elif int(c)==1 or c=="6":
                break
            else :
                print("กรุณากรอกหมายเลขสินค้าให้ถูกต้อง")
            except:
                print("กรุณากรอกหมายเลขสินค้าให้ถูกต้อง")
                pass

def show_item():
    for i in shop_list:
        if i == "BNK48 Photoset Shonichi":
            amount[0]+=1
        elif i == "BNK48 BADGE MERRY X'MAS":
            amount[1]+=1
        elif i == "BNK48 9th Single Senbatsu General Election Book":
            amount[2]+=1
        elif i == "CGM48 Towel":
            amount[3]+=1
        elif i == "BNK48 Belt Wristband : 2nd Generation The Debut":
            amount[4]+=1
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*250+amount[1]*200+amount[2]*380+amount[3]*380+amount[4]*144
    print("")
    print("{0:_<10}{1}{0:_<10}".format("","สินค้าที่คุณเลือกไปมีดังนี้"))
    print("{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}".format("","สินค้า","จำนวน","ราคา"))
    print("{0:_<38}".format(""))
    if amount[0]!=0:
        print("{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","111", str(amount[0]), str(amount[0]*250)))
    if amount[1]!=0:
        print('{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","222", str(amount[1]), str(amount[1]*200)))
    if amount[2]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","333", str(amount[2]), str(amount [2]*380)))
    if amount[3]!=0:
        print("{0:.<6}{1}{0:.<8}{2}{0:.<9}{3}{0:.<10}'.format("","444",str(amount[3]), str(amount[3]*380)))
    if amount[4]!=0:
        print("{0:.<6}{1}{0:.<3}{2}{0:.<9}{3}{0:.<10}'.format("","555", str(amount[4]),str(amount[4]*144)))
    print("{0:_<38}".format(""))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricett)))
    print("")
print("\tWelcome IAM48 Shop")
print('------------------------------------')

def pick_item()
while(True):
    print('1. แสดงสินค้ารายการ')
    print('2. หยิบสินค้าเข้าตะกร้า')
    print('3. เเสดงรายการสินค้าเเละราคาที่หยิบ')
    print('4. หยิบสินค้าออกจากตะกร้า')
    print('5. ปิดโปรเเกรม')
    print('')
    ch = input("กรุณาเลือกทำรายการ")
    if ch == "1" :
        list_item()
    elif ch=="2" :
        pick_item()
    elif ch=="3" :
        show_item()
    elif ch=="4" :
        out_item()
    elif ch=="5" :
        ch=input("ต้องการออกจากโปรเเกรมใช่หรือไม่ y/n: ")
        if ch == 'y' :
            break
        elif ch == 'n':
            continue