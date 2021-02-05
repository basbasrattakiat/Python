import datetime
now = datetime.datetime.now()
name_ = []
pts_ = []
time_ = []
hit = []

def menu():
    for i in range(num):
        name = input('กรอกชื่อ : ')
        pts = float(input('กรอกคะเเนน :  '))
        time = float(input('กรอกเวลาที่ใช้ :  '))
        hit.append(pts/time)
        name_.append(name)
        pts_.append(pts)
        time_.append(time)
    for i in range(num):
        j = i
        for j in range(num):
            if hit[i] > hit[j]:  #เรียงข้อมูลจากน้อยไปมาก
                a,b,c,d = hit[i], name_[i],pts_[i], time_[i]
                hit[i], name_[i],pts_[i], time_[i] = hit[j], name_[j], pts_[j], time_[j]
                hit[j],name_[j],pts_[j],time_[j] = a,b,c,d
def show():
    print('Shongun Sunday Training 2021')
    print('Condition : 1')
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print('{0: <10}{1: <10}{2: <10}{3: <18}{4: <15}{5: <15}{6: <10}'.format('NO.', 'PTS', 'TIME', 'COMPETITER3Name', 'HIT FACTOR', 'STATE POINTS', 'STATE PERCENT'))
    for i in range(num):
        SPS =hit[i]/hit[0]*50
        SPT =SPS/(hit[0]/hit[0]*50)*100
        print("{0: <10}{1: <10}{2: <10}{3: <18}{4: <15}{5: <15}{6: <10}" .format(i+i, int(pts_[i]),'%.2f'%time_[i], name_[i],'%.4f'%hit[i],'%.4f'%SPS,'%.2f'%SPT))
num = int(input('จำนวนผู้เข้าเเข่งขัน : '))
menu()
show()