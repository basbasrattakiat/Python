from tkinter import *
import tkinter as tk
import sqlite3
import time

window = Tk()
window.option_add('*Font' , '"DB HelvethaicaMon X bd" 20')
window.title ('EDTARO 16')
window.minsize (width=1200 , height=700)
thisdict = {}  #dic ข้อมูลการจองทั้งหมด
seatlock = {}  #dic เก็บข้อมูล ที่นั่ง จับกับ YES NO
seattext = []  #เก็บข้อมูลช่ั่วคราว เพื่อการส่งค่าไปเก็บใน หน้าบันทึกจองที่นั่่ง การเเสดงปุ่มทั้งหมด

def export_data_database () :
    try :
        conn = sqlite3.connect(r"D:\python\Project - Copy\data_11032021.db")
        c = conn.cursor()
        c.execute ('''SELECT * FROM edtaro''')
        result = c.fetchall()
        for x in result :
            #print ("ที่นั่ง : "+x[1]+"\tชื่อผู้จอง : "+x[2]+"\tเบอร์โทรศัพท์ : "+x[3])
            data_seat = str(x[1])
            data_name = str(x[2])
            data_tel = str(x[3]) 
            thisdict.update({data_tel : [data_name,data_seat] })

            if data_name != "" and data_tel != "" :
                seatlock.update({data_seat : ['YES'] })
            else :
                seatlock.update({data_seat : ['NO'] })
            #print (seatlock)
    except sqlite3.Error as e:
        print('ข้อมูล : นำเข้าไม่สำเร็จ',e)
    finally :
        if conn :
            conn.close ()

def booking_seat () :
    seatprint = [] #เพื่อเเสดงผลที่นั่งที่เลือก และมอบค่าให้การเก็บข้อมูล

    def text_for_button () :
        try :
            conn = sqlite3.connect(r"D:\python\Project - Copy\data_11032021.db")
            c = conn.cursor()
            c.execute ('''SELECT * FROM edtaro''')
            result = c.fetchall()
            for x in result :
                data_seat = str(x[1])
                seattext.append(data_seat)                
        except sqlite3.Error as e:
            print('ข้อมูล : นำเข้าไม่สำเร็จ',e)
        finally :
                if conn :
                    conn.close ()
                    
    def new_menu_booking_seat () :
        Frame (window, bg= '#f0f0f0', bd=5).place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.6, anchor='n')
        Label (window, text="จองที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
  
        nameblock = Label (window, text="กำลังเลือกจองที่นั่ง........ กรุณากรอกชื่อและเบอร์โทรศัพท์ หากข้อมูลถูกต้อง กด [บันทึกข้อมูลการจองที่นั่ง]",bg='#f0f0f0', bd=6)
        nameblock.place(relx=0.62, rely=0.45, relwidth=0.7, relheight=0.07, anchor='n')

        seat1 = Label (window, text="ตำแหน่งที่นั่ง\n"+seatprint[0],bg="#B22222" , fg="#FFFFFF")
        seat1.place(relx=0.4, rely=0.60, relwidth=0.15, relheight=0.15, anchor='n')
            
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.72, rely=0.60, relwidth=0.4, relheight=0.07, anchor='n')
                
        Label (frame, text="ชื่อผู้จอง").place(relwidth=0.3, relheight=1)

        textblock1 = tk.Entry(frame)
        textblock1.place(relx=0.31,relwidth=0.69, relheight=1) 

        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.72, rely=0.68, relwidth=0.4, relheight=0.07, anchor='n')
                
        Label (frame, text="เบอร์โทรศัพท์").place(relwidth=0.3, relheight=1)

        textblock2 = Entry (frame)
        textblock2.place(relx=0.31,relwidth=0.69, relheight=1)

        def new_update_seat () :
            data_name = str(textblock1.get())
            data_tel = str(textblock2.get())
            data_seat = str(seatprint[0])

            try :
                conn = sqlite3.connect(r"D:\python\Project - Copy\data_11032021.db")
                c = conn.cursor()
                data = (data_name,data_tel,data_seat)
                c.execute ('''UPDATE edtaro SET Name=?,Tel=? WHERE Seat=?''',data)
                conn.commit()
                c.close()
            except sqlite3.Error as e:
                print('การจองที่นั่ง : อัปเดตพบปัญหา',e)
            finally :
                if conn :
                    #print('การจองที่นั่ง : อัปเดตที่นั่งเรียบร้อย')
                    conn.close ()
                    
            #ดักเลือกที่นั่งแล้วไม่กรอกข้อมูล
            if data_name == "" and data_tel == "" :
                Label (window, text="⚠ ไม่มีข้อมูลการจองบันทึกเข้าสู่ฐานข้อมูล\n\nกรุณาทำการเลือกที่นั่งใหม่อีกครั้ง\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]",bg='#ffffff').place(relx=0.62, rely=0.45, relwidth=0.65, relheight=0.48, anchor='n')
            else :
                #, text="ชื่อผู้จอง  :  "+data_name+"\nเบอร์โทรศัพท์  :  "+data_tel+"\nที่นั่งที่จอง  :  "+data_seat
                #+"\n\n📒 บันทึกข้อมูลการจองเข้าสู่ฐานข้อมูลเรียบร้อย\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]",bg='#ffffff')

                localtime = time.asctime(time.localtime(time.time()))
                Label (window,bg="#FFFFFF").place(relx=0.62, rely=0.45, relwidth=0.65, relheight=0.48, anchor='n')
                
                Label (window,text = "บัตรเข้าชม",fg="#000000",bg ="#f0f0f0").place(relx=0.38, rely=0.48, relwidth=0.13, relheight=0.08, anchor='n')
                Label (window,bg ="#ffffff",text = "การแสดงละครเวทีคณะศึกษาศาสตร์ ED-TA-RO 16 \nกุหลาบปากซัน The Musical 2564",fg="#000000").place(relx=0.67,rely=0.48, anchor='n')
                
                Label (window,bg ="#7e0f15",fg="#ffffff",text ="ตำแหน่งที่นั่ง\n\n\n").place(relx=0.38 ,rely=0.6, relwidth=0.13, relheight=0.18, anchor='n') #สีแดง
                Label (window,bg ="#ffffff",fg="#000000",text =data_seat).place(relx=0.38, rely=0.67, relwidth=0.06, relheight=0.08, anchor='n') #สี่เหลี่ยมใน
                
                Label (window,bg="#f0f0f0").place(relx=0.68,rely=0.60,relwidth=0.45, relheight=0.08,anchor='n') #ชื่อผู้จอง
                Label (window,bg="#f0f0f0").place(relx=0.68,rely=0.7,relwidth=0.45, relheight=0.08,anchor='n') #เบอร์โทร
                Label (window,fg="#000000",bg ="#f0f0f0",text ="ชื่อผู้จอง").place(relx=0.54,rely=0.62, anchor='n')
                Label (window,fg="#000000",bg ="#f0f0f0",text ="เบอร์โทร").place(relx=0.54,rely=0.72, anchor='n') 
                Label (window,fg="#000000",bg ="#ffffff",text =data_name).place(relx=0.7,rely=0.62,relwidth=0.2,anchor='n') #dataชื่อ
                Label (window,fg="#000000",bg ="#ffffff",text =data_tel).place(relx=0.7,rely=0.72,relwidth=0.2,anchor='n') #dataเบอร์

                Label (window,fg="#000000",bg ="#ffffff",text ="**กรุณาเก็บหลักฐานการจองที่นั่ง**\nด้วยการถ่ายภาพหน้าจอแสดงผลนี้ เพื่อรับบัตรชมละครในวันทำการแสดง").place(relx=0.52,rely=0.83,relwidth=0.4, anchor='n')
                Label (window,text=localtime).place(relx=0.83, rely=0.83, relwidth=0.2, relheight=0.07, anchor='n')

            print('เก็บข้อมูลการจองเข้าตัวแปรแล้ว : '+data_name+' '+data_tel)
            thisdict.update({data_tel : [data_name,data_seat]})

            #Label (window , image=PhotoImage(file="end - Copy.png")).place(relx=0.6, rely=0.40)
    
        Button (window,text='บันทึกข้อมูลการจองที่นั่ง',bg="#5c0606" , fg="#FFFFFF",command=new_update_seat).place(relx=0.62,rely=0.85, relwidth=0.4, anchor='n')  

    def button () :
        def comfrim(saetreturn) :
            Frame(window, bg= '#f0f0f0', bd=5).place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.6, anchor='n')
            Label (window, text="จองที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
            Label (window, text="ยึนยันการเลือกที่นั่ง\n"+saetreturn, bg='#FFFFFF',fg="#000000", bd=6).place(relx=0.62, rely=0.55, relwidth=0.6, relheight=0.18, anchor='n')
            Button(window,text='ตกลง', bg="#5c0606" , fg="#FFFFFF",command=new_menu_booking_seat).place(relx=0.49,rely=0.80, relwidth=0.2, anchor='n')
            Button(window,text='ยกเลิก', bg="#5c0606" , fg="#FFFFFF",command=booking_seat).place(relx=0.75,rely=0.80, relwidth=0.2, anchor='n')
        def A01 () :
            seat_button = Button (window, text=seattext[1] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[1]),comfrim(seatprint[0])])
            if seatlock [str(seattext[1])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A02 () :
            seat_button = Button (window, text=seattext[2] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[2]),comfrim(seatprint[0])])
            if seatlock [str(seattext[2])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A03 () :
            seat_button = Button (window, text=seattext[3] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[3]),comfrim(seatprint[0])])
            if seatlock [str(seattext[3])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A04 () :
            seat_button = Button (window, text=seattext[4] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[4]),comfrim(seatprint[0])])
            if seatlock [str(seattext[4])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A05 () :
            seat_button = Button (window, text=seattext[5] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[5]),comfrim(seatprint[0])])
            if seatlock [str(seattext[5])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A06 () :
            seat_button = Button (window, text=seattext[6] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[6]),comfrim(seatprint[0])])
            if seatlock [str(seattext[6])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')  
        def A07 () :
            seat_button = Button (window, text=seattext[7] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[7]),comfrim(seatprint[0])])
            if seatlock [str(seattext[7])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n') 
        def A08 () :
            seat_button = Button (window, text=seattext[8] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[8]),comfrim(seatprint[0])])
            if seatlock [str(seattext[8])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A09 () :
            seat_button = Button (window, text=seattext[9] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[9]),comfrim(seatprint[0])])
            if seatlock [str(seattext[9])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')     
        def A10 () :
            seat_button = Button (window, text=seattext[10] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[10]),comfrim(seatprint[0])])
            if seatlock [str(seattext[10])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')  
        def A11 () :
            seat_button = Button (window, text=seattext[11] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[11]),comfrim(seatprint[0])])
            if seatlock [str(seattext[11])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A12 () :
            seat_button = Button (window, text=seattext[12] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[12]),comfrim(seatprint[0])])
            if seatlock [str(seattext[12])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A13 () :
            seat_button = Button (window, text=seattext[13] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[13]),comfrim(seatprint[0])])
            if seatlock [str(seattext[13])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A14 () :
            seat_button = Button (window, text=seattext[14] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[14]),comfrim(seatprint[0])])
            if seatlock [str(seattext[14])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        def A15 () :
            seat_button = Button (window, text=seattext[15] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[15]),comfrim(seatprint[0])])
            if seatlock [str(seattext[15])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.62, relwidth=0.035, relheight=0.03, anchor='n')
        
        def B01 () :
            seat_button = Button (window, text=seattext[16] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[16]),comfrim(seatprint[0])])
            if seatlock [str(seattext[16])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B02 () :
            seat_button = Button (window, text=seattext[17] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[17]),comfrim(seatprint[0])])
            if seatlock [str(seattext[17])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B03 () :
            seat_button = Button (window, text=seattext[18] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[18]),comfrim(seatprint[0])])
            if seatlock [str(seattext[18])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B04 () :
            seat_button = Button (window, text=seattext[19] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[19]),comfrim(seatprint[0])])
            if seatlock [str(seattext[19])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B05 () :
            seat_button = Button (window, text=seattext[20] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[20]),comfrim(seatprint[0])])
            if seatlock [str(seattext[20])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B06 () :
            seat_button = Button (window, text=seattext[21] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[21]),comfrim(seatprint[0])])
            if seatlock [str(seattext[21])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')  
        def B07 () :
            seat_button = Button (window, text=seattext[22] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[22]),comfrim(seatprint[0])])
            if seatlock [str(seattext[22])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n') 
        def B08 () :
            seat_button = Button (window, text=seattext[23] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[23]),comfrim(seatprint[0])])
            if seatlock [str(seattext[23])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B09 () :
            seat_button = Button (window, text=seattext[24] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[24]),comfrim(seatprint[0])])
            if seatlock [str(seattext[24])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B10 () :
            seat_button = Button (window, text=seattext[25] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[25]),comfrim(seatprint[0])])
            if seatlock [str(seattext[25])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')  
        def B11 () :
            seat_button = Button (window, text=seattext[26] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[26]),comfrim(seatprint[0])])
            if seatlock [str(seattext[26])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B12 () :
            seat_button = Button (window, text=seattext[27] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[27]),comfrim(seatprint[0])])
            if seatlock [str(seattext[27])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B13 () :
            seat_button = Button (window, text=seattext[28] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[28]),comfrim(seatprint[0])])
            if seatlock [str(seattext[28])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B14 () :
            seat_button = Button (window, text=seattext[29] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[29]),comfrim(seatprint[0])])
            if seatlock [str(seattext[29])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')
        def B15 () :
            seat_button = Button (window, text=seattext[30] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[30]),comfrim(seatprint[0])])
            if seatlock [str(seattext[30])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.66, relwidth=0.035, relheight=0.03, anchor='n')

        def C01 () :
            seat_button = Button (window, text=seattext[31] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[31]),comfrim(seatprint[0])])
            if seatlock [str(seattext[31])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C02 () :
            seat_button = Button (window, text=seattext[32] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[32]),comfrim(seatprint[0])])
            if seatlock [str(seattext[32])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C03 () :
            seat_button = Button (window, text=seattext[33] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[33]),comfrim(seatprint[0])])
            if seatlock [str(seattext[33])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C04 () :
            seat_button = Button (window, text=seattext[34] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[34]),comfrim(seatprint[0])])
            if seatlock [str(seattext[34])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C05 () :
            seat_button = Button (window, text=seattext[35] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[35]),comfrim(seatprint[0])])
            if seatlock [str(seattext[35])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C06 () :
            seat_button = Button (window, text=seattext[36] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[36]),comfrim(seatprint[0])])
            if seatlock [str(seattext[36])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')  
        def C07 () :
            seat_button = Button (window, text=seattext[37] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[37]),comfrim(seatprint[0])])
            if seatlock [str(seattext[37])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n') 
        def C08 () :
            seat_button = Button (window, text=seattext[38] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[38]),comfrim(seatprint[0])])
            if seatlock [str(seattext[38])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C09 () :
            seat_button = Button (window, text=seattext[39] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[39]),comfrim(seatprint[0])])
            if seatlock [str(seattext[39])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')     
        def C10 () :
            seat_button = Button (window, text=seattext[40] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[40]),comfrim(seatprint[0])])
            if seatlock [str(seattext[40])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')  
        def C11 () :
            seat_button = Button (window, text=seattext[41] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[41]),comfrim(seatprint[0])])
            if seatlock [str(seattext[41])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C12 () :
            seat_button = Button (window, text=seattext[42] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[42]),comfrim(seatprint[0])])
            if seatlock [str(seattext[42])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C13 () :
            seat_button = Button (window, text=seattext[43] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[43]),comfrim(seatprint[0])])
            if seatlock [str(seattext[43])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C14 () :
            seat_button = Button (window, text=seattext[44] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[44]),comfrim(seatprint[0])])
            if seatlock [str(seattext[44])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        def C15 () :
            seat_button = Button (window, text=seattext[45] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[45]),comfrim(seatprint[0])])
            if seatlock [str(seattext[45])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.7, relwidth=0.035, relheight=0.03, anchor='n')
        
        def D01 () :
            seat_button = Button (window, text=seattext[46] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[46]),comfrim(seatprint[0])])
            if seatlock [str(seattext[46])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D02 () :
            seat_button = Button (window, text=seattext[47] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[47]),comfrim(seatprint[0])])
            if seatlock [str(seattext[47])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D03 () :
            seat_button = Button (window, text=seattext[48] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[48]),comfrim(seatprint[0])])
            if seatlock [str(seattext[48])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D04 () :
            seat_button = Button (window, text=seattext[49] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[49]),comfrim(seatprint[0])])
            if seatlock [str(seattext[49])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D05 () :
            seat_button = Button (window, text=seattext[50] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[50]),comfrim(seatprint[0])])
            if seatlock [str(seattext[50])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D06 () :
            seat_button = Button (window, text=seattext[51] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[51]),comfrim(seatprint[0])])
            if seatlock [str(seattext[51])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')  
        def D07 () :
            seat_button = Button (window, text=seattext[52] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[52]),comfrim(seatprint[0])])
            if seatlock [str(seattext[52])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n') 
        def D08 () :
            seat_button = Button (window, text=seattext[53] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[53]),comfrim(seatprint[0])])
            if seatlock [str(seattext[53])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D09 () :
            seat_button = Button (window, text=seattext[54] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[54]),comfrim(seatprint[0])])
            if seatlock [str(seattext[54])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D10 () :
            seat_button = Button (window, text=seattext[55] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[55]),comfrim(seatprint[0])])
            if seatlock [str(seattext[55])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')  
        def D11 () :
            seat_button = Button (window, text=seattext[56] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[56]),comfrim(seatprint[0])])
            if seatlock [str(seattext[56])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D12 () :
            seat_button = Button (window, text=seattext[57] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[57]),comfrim(seatprint[0])])
            if seatlock [str(seattext[57])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D13 () :
            seat_button = Button (window, text=seattext[58] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[58]),comfrim(seatprint[0])])
            if seatlock [str(seattext[58])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D14 () :
            seat_button = Button (window, text=seattext[59] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[59]),comfrim(seatprint[0])])
            if seatlock [str(seattext[59])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')
        def D15 () :
            seat_button = Button (window, text=seattext[60] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[60]),comfrim(seatprint[0])])
            if seatlock [str(seattext[60])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.74, relwidth=0.035, relheight=0.03, anchor='n')

        def E01 () :
            seat_button = Button (window, text=seattext[61] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[61]),comfrim(seatprint[0])])
            if seatlock [str(seattext[61])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E02 () :
            seat_button = Button (window, text=seattext[62] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[62]),comfrim(seatprint[0])])
            if seatlock [str(seattext[62])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E03 () :
            seat_button = Button (window, text=seattext[63] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[63]),comfrim(seatprint[0])])
            if seatlock [str(seattext[63])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E04 () :
            seat_button = Button (window, text=seattext[64] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[64]),comfrim(seatprint[0])])
            if seatlock [str(seattext[64])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E05 () :
            seat_button = Button (window, text=seattext[65] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[65]),comfrim(seatprint[0])])
            if seatlock [str(seattext[65])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E06 () :
            seat_button = Button (window, text=seattext[66] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[66]),comfrim(seatprint[0])])
            if seatlock [str(seattext[66])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')  
        def E07 () :
            seat_button = Button (window, text=seattext[67] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[67]),comfrim(seatprint[0])])
            if seatlock [str(seattext[67])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n') 
        def E08 () :
            seat_button = Button (window, text=seattext[68] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[68]),comfrim(seatprint[0])])
            if seatlock [str(seattext[68])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E09 () :
            seat_button = Button (window, text=seattext[69] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[69]),comfrim(seatprint[0])])
            if seatlock [str(seattext[69])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')     
        def E10 () :
            seat_button = Button (window, text=seattext[70] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[70]),comfrim(seatprint[0])])
            if seatlock [str(seattext[70])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')  
        def E11 () :
            seat_button = Button (window, text=seattext[71] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[71]),comfrim(seatprint[0])])
            if seatlock [str(seattext[71])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E12 () :
            seat_button = Button (window, text=seattext[72] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[72]),comfrim(seatprint[0])])
            if seatlock [str(seattext[72])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E13 () :
            seat_button = Button (window, text=seattext[73] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[73]),comfrim(seatprint[0])])
            if seatlock [str(seattext[73])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E14 () :
            seat_button = Button (window, text=seattext[74] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[74]),comfrim(seatprint[0])])
            if seatlock [str(seattext[74])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        def E15 () :
            seat_button = Button (window, text=seattext[75] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[75]),comfrim(seatprint[0])])
            if seatlock [str(seattext[75])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.78, relwidth=0.035, relheight=0.03, anchor='n')
        
        def F01 () :
            seat_button = Button (window, text=seattext[76] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[76]),comfrim(seatprint[0])])
            if seatlock [str(seattext[76])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F02 () :
            seat_button = Button (window, text=seattext[77] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[77]),comfrim(seatprint[0])])
            if seatlock [str(seattext[77])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F03 () :
            seat_button = Button (window, text=seattext[78] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[78]),comfrim(seatprint[0])])
            if seatlock [str(seattext[78])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F04 () :
            seat_button = Button (window, text=seattext[79] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[79]),comfrim(seatprint[0])])
            if seatlock [str(seattext[79])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F05 () :
            seat_button = Button (window, text=seattext[80] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[80]),comfrim(seatprint[0])])
            if seatlock [str(seattext[80])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F06 () :
            seat_button = Button (window, text=seattext[81] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[81]),comfrim(seatprint[0])])
            if seatlock [str(seattext[81])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')  
        def F07 () :
            seat_button = Button (window, text=seattext[82] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[82]),comfrim(seatprint[0])])
            if seatlock [str(seattext[82])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n') 
        def F08 () :
            seat_button = Button (window, text=seattext[83] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[83]),comfrim(seatprint[0])])
            if seatlock [str(seattext[83])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F09 () :
            seat_button = Button (window, text=seattext[84] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[84]),comfrim(seatprint[0])])
            if seatlock [str(seattext[84])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F10 () :
            seat_button = Button (window, text=seattext[85] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[85]),comfrim(seatprint[0])])
            if seatlock [str(seattext[85])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')  
        def F11 () :
            seat_button = Button (window, text=seattext[86] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[86]),comfrim(seatprint[0])])
            if seatlock [str(seattext[86])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F12 () :
            seat_button = Button (window, text=seattext[87] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[87]),comfrim(seatprint[0])])
            if seatlock [str(seattext[87])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F13 () :
            seat_button = Button (window, text=seattext[88] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[88]),comfrim(seatprint[0])])
            if seatlock [str(seattext[88])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F14 () :
            seat_button = Button (window, text=seattext[89] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[89]),comfrim(seatprint[0])])
            if seatlock [str(seattext[89])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')
        def F15 () :
            seat_button = Button (window, text=seattext[90] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[90]),comfrim(seatprint[0])])
            if seatlock [str(seattext[90])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.82, relwidth=0.035, relheight=0.03, anchor='n')

        def G01 () :
            seat_button = Button (window, text=seattext[91] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[91]),comfrim(seatprint[0])])
            if seatlock [str(seattext[91])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G02 () :
            seat_button = Button (window, text=seattext[92] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[92]),comfrim(seatprint[0])])
            if seatlock [str(seattext[92])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G03 () :
            seat_button = Button (window, text=seattext[93] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[93]),comfrim(seatprint[0])])
            if seatlock [str(seattext[93])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G04 () :
            seat_button = Button (window, text=seattext[94] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[94]),comfrim(seatprint[0])])
            if seatlock [str(seattext[94])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G05 () :
            seat_button = Button (window, text=seattext[95] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[95]),comfrim(seatprint[0])])
            if seatlock [str(seattext[95])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G06 () :
            seat_button = Button (window, text=seattext[96] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[96]),comfrim(seatprint[0])])
            if seatlock [str(seattext[96])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')  
        def G07 () :
            seat_button = Button (window, text=seattext[97] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[97]),comfrim(seatprint[0])])
            if seatlock [str(seattext[97])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n') 
        def G08 () :
            seat_button = Button (window, text=seattext[98] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[98]),comfrim(seatprint[0])])
            if seatlock [str(seattext[98])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G09 () :
            seat_button = Button (window, text=seattext[99] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[99]),comfrim(seatprint[0])])
            if seatlock [str(seattext[99])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')     
        def G10 () :
            seat_button = Button (window, text=seattext[100] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[100]),comfrim(seatprint[0])])
            if seatlock [str(seattext[100])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')  
        def G11 () :
            seat_button = Button (window, text=seattext[101] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[101]),comfrim(seatprint[0])])
            if seatlock [str(seattext[101])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G12 () :
            seat_button = Button (window, text=seattext[102] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[102]),comfrim(seatprint[0])])
            if seatlock [str(seattext[102])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G13 () :
            seat_button = Button (window, text=seattext[103] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[103]),comfrim(seatprint[0])])
            if seatlock [str(seattext[103])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G14 () :
            seat_button = Button (window, text=seattext[104] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[104]),comfrim(seatprint[0])])
            if seatlock [str(seattext[104])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        def G15 () :
            seat_button = Button (window, text=seattext[105] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[105]),comfrim(seatprint[0])])
            if seatlock [str(seattext[105])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.86, relwidth=0.035, relheight=0.03, anchor='n')
        
        def H01 () :
            seat_button = Button (window, text=seattext[106] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[106]),comfrim(seatprint[0])])
            if seatlock [str(seattext[106])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.315, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H02 () :
            seat_button = Button (window, text=seattext[107] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[107]),comfrim(seatprint[0])])
            if seatlock [str(seattext[107])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.355, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H03 () :
            seat_button = Button (window, text=seattext[108] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[108]),comfrim(seatprint[0])])
            if seatlock [str(seattext[108])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.395, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H04 () :
            seat_button = Button (window, text=seattext[109] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[109]),comfrim(seatprint[0])])
            if seatlock [str(seattext[109])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.435, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H05 () :
            seat_button = Button (window, text=seattext[110] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[110]),comfrim(seatprint[0])])
            if seatlock [str(seattext[110])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.475, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H06 () :
            seat_button = Button (window, text=seattext[111] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[111]),comfrim(seatprint[0])])
            if seatlock [str(seattext[111])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.540, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')  
        def H07 () :
            seat_button = Button (window, text=seattext[112] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[112]),comfrim(seatprint[0])])
            if seatlock [str(seattext[112])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.580, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n') 
        def H08 () :
            seat_button = Button (window, text=seattext[113] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[113]),comfrim(seatprint[0])])
            if seatlock [str(seattext[113])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.620, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H09 () :
            seat_button = Button (window, text=seattext[114] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[114]),comfrim(seatprint[0])])
            if seatlock [str(seattext[114])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.660, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H10 () :
            seat_button = Button (window, text=seattext[115] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[115]),comfrim(seatprint[0])])
            if seatlock [str(seattext[115])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.700, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')  
        def H11 () :
            seat_button = Button (window, text=seattext[116] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[116]),comfrim(seatprint[0])])
            if seatlock [str(seattext[116])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.765, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H12 () :
            seat_button = Button (window, text=seattext[117] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[117]),comfrim(seatprint[0])])
            if seatlock [str(seattext[117])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.805, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H13 () :
            seat_button = Button (window, text=seattext[118] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[118]),comfrim(seatprint[0])])
            if seatlock [str(seattext[118])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.845, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H14 () :
            seat_button = Button (window, text=seattext[119] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[119]),comfrim(seatprint[0])])
            if seatlock [str(seattext[119])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.885, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')
        def H15 () :
            seat_button = Button (window, text=seattext[120] , bg="#5c0606" , fg="#FFFFFF",bd=0 ,command=lambda: [seatprint.append(seattext[120]),comfrim(seatprint[0])])
            if seatlock [str(seattext[120])] == ['YES'] :
                seat_button = Button (window, text="X" , bg="#BBBBBB" , fg="#FFFFFF",bd=0)
            seat_button.place (relx = 0.925, rely = 0.9, relwidth=0.035, relheight=0.03, anchor='n')

        A01(),A02(),A03(),A04(),A05(),A06(),A07(),A08(),A09(),A10(),A11(),A12(),A13(),A14(),A15(),
        B01(),B02(),B03(),B04(),B05(),B06(),B07(),B08(),B09(),B10(),B11(),B12(),B13(),B14(),B15(),
        C01(),C02(),C03(),C04(),C05(),C06(),C07(),C08(),C09(),C10(),C11(),C12(),C13(),C14(),C15(),
        D01(),D02(),D03(),D04(),D05(),D06(),D07(),D08(),D09(),D10(),D11(),D12(),D13(),D14(),D15(),
        E01(),E02(),E03(),E04(),E05(),E06(),E07(),E08(),E09(),E10(),E11(),E12(),E13(),E14(),E15(),
        F01(),F02(),F03(),F04(),F05(),F06(),F07(),F08(),F09(),F10(),F11(),F12(),F13(),F14(),F15(),
        G01(),G02(),G03(),G04(),G05(),G06(),G07(),G08(),G09(),G10(),G11(),G12(),G13(),G14(),G15(),
        H01(),H02(),H03(),H04(),H05(),H06(),H07(),H08(),H09(),H10(),H11(),H12(),H13(),H14(),H15()

    def headmenu_booking_seat () :
        Frame (window, bg= '#f0f0f0', bd=5).place(relx=0.62, rely=0.35, relwidth=0.67, relheight=0.70, anchor='n')
        Label (window, text="จองที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
        Label (window, text="กรุณากดเลือกที่นั่งที่ต้องการ เพื่อเข้าสู่หน้าบันทึกข้อมูลผู้จอง", bg='#f0f0f0', bd=6).place(relx=0.62, rely=0.45, relwidth=0.7, relheight=0.07, anchor='n')
        Label (window, text="เวที",bg="#FFFFFF").place(relx=0.62, rely=0.54, relwidth=0.65, relheight=0.06, anchor='n')
    
    export_data_database ()
    headmenu_booking_seat ()
    text_for_button()
    button ()
    
def search_seat () :
    def adddata_search__seat() :
        #รับข้อมูลเบอร์โทรศัพท์
        frame = tk.Frame(window, bg='#828282', bd=6)
        frame.place(relx=0.62, rely=0.55, relwidth=0.6, relheight=0.07, anchor='n')
            
        Label (frame, text="เบอร์โทรศัพท์").place(relwidth=0.3, relheight=1)

        textblock = Entry(frame)
        textblock.place(relx=0.31,relwidth=0.69, relheight=1)

        def search() :
            frame = tk.Frame(window, bg='#FFFFFF', bd=6)
            frame.place(relx=0.62, rely=0.45, relwidth=0.65, relheight=0.48, anchor='n')
            data_tel = str(textblock.get())
            #print("\nผลการค้นหา : ชื่อผู้จอง\t-- ตำแหน่งที่นั่ง")

            if data_tel == "" :
                Label (frame, text="⚠ กรุณากรอกเบอร์โทรศัพท์ใหม่อีกครั้ง\nออกจากหน้านี้ กด [กลับสู่หน้าหลัก]",bg='#FFFFFF', fg = '#000000').place(relwidth=1, relheight=1)
            else :
                try :
                    search_output = thisdict[data_tel]
                    #print("ชื่อ : "+search_output[0]+"\t -- ตำแหน่งที่นั่งที่จอง : "+search_output[1])

                except Exception as e : print('ผลการค้นหา : พบข้อมูล {}',e)

                finally :
                    
                    Label (frame, text="⚠ ไม่พบข้อมูลการค้นหา",bg='#FFFFFF', fg = '#000000').place(relwidth=1, relheight=1)
                    try : 
                        Label (frame, text="📒 ผลการค้นหาที่นั่ง\nชื่อ  :  "+search_output[0]+"\nตำแหน่งที่นั่งที่จอง  :  "
                        +search_output[1]+"\n\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]"
                        ,bg='#FFFFFF', fg = '#000000').place(relwidth=1, relheight=1)

                    except Exception as e: print('ผลการค้นหา : ไม่พบข้อมูล {}',e)
                    finally : print('เตือน : เสร็จสิ้นการค้นหา')
                
        #ปุ่มค้นหาที่นั่ง
        Button(window,text='ค้นหาที่นั่ง',bg="#5c0606" , fg="#FFFFFF",command=search).place(relx=0.62,rely=0.85, relwidth=0.5, anchor='n')
    def head_search_seat() :
        w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
        w_screen.place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.6, anchor='n')
        
        Label (window, text="ค้นหาที่นั่ง",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')
        
        frame = tk.Frame(window, bg='#f0f0f0', bd=6)
        frame.place(relx=0.62, rely=0.45, relwidth=0.7, relheight=0.07, anchor='n')
                        
        nameblock = Label (frame, text="กรุณากรอกเบอร์โทรศัพท์ เพื่อค้นหาข้อมูลตำแหน่งที่จอง หากข้อมูลถูกต้อง กด [ค้นหาที่นั่ง]")
        nameblock.place(relwidth=1, relheight=1)
    
    export_data_database ()
    head_search_seat()
    adddata_search__seat()

def head_app () : #เสร็จแล้ว
    Label (window, text="โปรเเกรมจองที่นั่งละครเวทีคณะศึกษาศาสตร์ ED-TA-RO 16 กุหลาบปากซัน The Musical 2564",width=200 , bg="#7e0f15" , fg="#FFFFFF").pack()
    Label (window, text="Develop by Computer Education 17 | Khon Kean University",width=200 , bg="#7e0f15" , fg="#FFFFFF").pack()
    Label (window, text="",width=200 , bg="#B22222").pack()

def admin () :  #เสร็จเเล้ว
    def clean_screen_admin() :
        w_screen = tk.Frame(window, bg= '#f0f0f0', bd=5)
        w_screen.place(relx=0.62, rely=0.35, relwidth=0.67, relheight=0.70, anchor='n')
    def login() :
        def munu_login() :
            frame = tk.Frame(window, bg='#828282', bd=6)
            frame.place(relx=0.62, rely=0.5, relwidth=0.4, relheight=0.07, anchor='n')
            nameblock = Label (frame, text="กรุณาใส่รหัสผ่าน")
            nameblock.place(relwidth=0.3, relheight=1)
            textblock = tk.Entry(frame, show="*")
            textblock.place(relx=0.31,relwidth=0.69, relheight=1)

            def checkpass() :
                password = str(textblock.get())
                if password=='comed17' :
                    import os
                    Frame (window, bg= '#f0f0f0', bd=5).place(relx=0.62, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')
                    Label (window, text="ผู้ดูแลระบบ",bg="#1C1C1C" , fg="#FFFFFF").place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.08, anchor='n')

                    Label (window, bg="#ffffff").place(relx=0.73, rely=0.5, relwidth=0.42, relheight=0.26, anchor='n')
                    Label (window, bg='#ffffff').place(relx=0.62, rely=0.79, relwidth=0.65, relheight=0.15, anchor='n')
                    
                    def openSQLite():
                        filename = '"D:\\python\\Project - Copy\\data_11032021.db"'
                        os.system(filename)

                    def delete_all () :
                        data_name = str("")
                        data_tel = str("")
                        data_ID = str('0')
                        Label (window, bg="#ffffff").place(relx=0.73, rely=0.5, relwidth=0.42, relheight=0.26, anchor='n')
                        def delete() :
                            try :
                                for data_ID in range(250):
                                    conn = sqlite3.connect(r"D:\python\Project - Copy\data_11032021.db")
                                    c = conn.cursor()
                                    data = (data_name,data_tel,data_ID)
                                    c.execute ('''UPDATE edtaro SET Name=?,Tel=? WHERE ID=?''',data)
                                    conn.commit()
                                    c.close()
                                    data_ID = data_ID+1
                            finally :
                                localtime = time.asctime(time.localtime(time.time()))
                                Label (window, text="ล้างข้อมูลการจองทั้งหมดสำเร็จ\n@"+localtime+"\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]",bg='#ffffff').place(relx=0.62, rely=0.79, relwidth=0.65, relheight=0.15, anchor='n')
        
                        Button (window,text='ยึนยันลบข้อมูลจองที่นั่ง',bg="#5c0606" , fg="#FFFFFF",command=delete).place(relx=0.72, rely=0.6, relwidth=0.3, relheight=0.07, anchor='n')


                    def delete_select() :
                        Label (window, bg="#ffffff").place(relx=0.73, rely=0.5, relwidth=0.42, relheight=0.26, anchor='n')

                        frame = tk.Frame(window, bg='#828282', bd=6)
                        frame.place(relx=0.72, rely=0.55, relwidth=0.3, relheight=0.07, anchor='n')
                        
                        Label (frame, text="ที่นั่ง").place(relwidth=0.3, relheight=1)

                        textblock5 = Entry (frame)
                        textblock5.place(relx=0.31,relwidth=0.69, relheight=1)

                        def del_se() :
                            data_name = str("")
                            data_tel = str("")
                            data_seat = str(textblock5.get())
                            try :
                                conn = sqlite3.connect(r"D:\python\Project - Copy\data_11032021.db")
                                c = conn.cursor()
                                data = (data_name,data_tel,data_seat)
                                c.execute ('''UPDATE edtaro SET Name=?,Tel=? WHERE Seat=?''',data)
                                conn.commit()
                                c.close()
                            finally :
                                localtime = time.asctime(time.localtime(time.time()))
                                Label (window, text="ล้างข้อมูลการจองที่นั่ง "+data_seat+" สำเร็จ\n@"+localtime+"\nออกจากหน้านี้ กดเลือกเมนู [กลับสู่หน้าหลัก]",bg='#ffffff').place(relx=0.62, rely=0.79, relwidth=0.65, relheight=0.15, anchor='n')
                                                
                        Button (window,text='ยึนยันลบข้อมูลจองที่นั่ง',bg="#5c0606" , fg="#FFFFFF",command=del_se).place(relx=0.72, rely=0.65, relwidth=0.3, relheight=0.07, anchor='n')

                    def munu_admin():
                        Button(window,text='เปิดฐานข้อมูล จาก SQLite', bg="#000000" , fg="#FFFFFF",command=openSQLite).place(relx=0.4,rely=0.5, relwidth=0.2, anchor='n')
                        Button(window,text='ลบข้อมูลการจองที่นั่ง (ทั้งหมด)', bg="#000000" , fg="#FFFFFF",command=delete_all).place(relx=0.4,rely=0.6, relwidth=0.2, anchor='n')
                        Button(window,text='ลบข้อมูลการจองที่นั่ง (ตำแหน่ง)', bg="#000000" , fg="#FFFFFF",command=delete_select).place(relx=0.4,rely=0.7, relwidth=0.2, anchor='n')

                    munu_admin()
                else :
                    Frame(window, bg= '#f0f0f0', bd=5).place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.58, anchor='n')

                    frame = tk.Frame(window, bg='#f0f0f0', bd=6)
                    frame.place(relx=0.6, rely=0.6, relwidth=0.6, relheight=0.07, anchor='n')
                    
                    nameblock = Label (frame, text="รหัสผ่านไม่ถูกต้อง")
                    nameblock.place(relwidth=1, relheight=1)
            
            def button_login() :
                button = tk.Button(window,text='เข้าสู่ระบบ',bg="#5c0606" , fg="#FFFFFF",command=checkpass)
                button.place(relx=0.62,rely=0.70, relwidth=0.3, anchor='n')

            button_login()
        munu_login()
    clean_screen_admin()
    login()   

def home () : #เสร็จแล้ว
    Frame (window, bg= '#f0f0f0', bd=5).place(relx=0.6, rely=0.35, relwidth=0.7, relheight=0.6, anchor='n')
    frame = Frame(window, bg='#ffffff', bd=6)
    frame.place(relx=0.62, rely=0.35, relwidth=0.65, relheight=0.34, anchor='n')

    textblock = Label (frame, text="คำแนะนำการใช้โปรเเกรม\n---------------------\nเลือกเมนูที่ต้องการใช้งาน หากสิ้นสุดการทำงาน กดเลือกเมนู [กลับสู่หน้าหลัก] หรือ [ออกจากโปรแกรม]\n\nภาคเรียนที่ 2  ปีการศึกษา 2563\nสาขาวิชาคอมพิวเตอร์ศึกษา คณะศึกษาศาสตร์ มหาวิทยาลัยขอนแก่น",bg="#FFFFFF")
    textblock.place(relwidth=1, relheight=1)

    name = Frame(window, bg='#1C1C1C', bd=6)
    name.place(relx=0.62, rely=0.71, relwidth=0.65, relheight=0.22, anchor='n')

    textblock = Label (name, text="จัดทำโดย\n1.นางสาวจิรดา บุญหนัก  รหัสนักศึกษา 633050128-3\n2.นายรัฐเกียรติ หริ่มเพ็ง  รหัสนักศึกษา 633050137-2",bg="#1C1C1C",fg="#FFFFFF",bd=1)
    textblock.place(relwidth=1, relheight=1)

def exit_app () : #เสร็จแล้ว
    Frame(window, bg= '#f0f0f0', bd=5).place(relx=0.62, rely=0.35, relwidth=0.67, relheight=0.70, anchor='n')
    
    frame = tk.Frame(window, bg='#f0f0f0', bd=6)
    frame.place(relx=0.62, rely=0.50, relwidth=0.6, relheight=0.07, anchor='n')
    
    Label (frame, text="ยืนยันการปิดโปรแกรม").place(relwidth=1, relheight=1)
    Button (window,text='ตกลง', bg="#5c0606" , fg="#FFFFFF",command=window.destroy).place(relx=0.49,rely=0.60, relwidth=0.2, anchor='n')
    Button (window,text='ยกเลิก', bg="#5c0606" , fg="#FFFFFF",command=home).place(relx=0.75,rely=0.60, relwidth=0.2, anchor='n')

def main_menu () : #เสร็จเเล้ว
    Frame (window, bg= '#FFFFFF', bd=5).place(relx=0.1, rely=0.1, relwidth=0.3, relheight=1, anchor='n')
    Label (window, text='😃 WELCOME'   , bg="#B22222" , fg="#ffffff", width=15, borderwidth=1)  .place(relx=0.12, rely=0.35, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='🏠 กลับสู่หน้าหลัก'   , bg="#B22222" , fg="#ffffff", width=15, borderwidth=1, command=home)       .place(relx=0.12, rely=0.45, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='🪑 จองที่นั่ง'       , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1, command=booking_seat)    .place(relx=0.12, rely=0.55, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='🔎 ค้นหาที่นั่ง'      , bg="#B22222" , fg="#FFFFFF", width=15, borderwidth=1 , command=search_seat)   .place(relx=0.12, rely=0.65, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='⛔ ออกจากโปรแกรม' , bg="#5c0606" , fg="#ffffff", width=15, borderwidth=1, command=exit_app)      .place(relx=0.12, rely=0.75, relwidth=0.18, relheight=0.08, anchor='n')
    Button (window, text='🔐 ผู้ดูแลระบบ'     , bg="#5c0606" , fg="#ffffff" , width=15, borderwidth=1, command=admin)         .place(relx=0.12, rely=0.85, relwidth=0.18, relheight=0.08, anchor='n')
    
def final () : #เสร็จเเล้ว
    main_menu()
    photo = PhotoImage(file="logo.png")
    Label (window , image=photo , borderwidth=0).pack()
    head_app()
    home()
    window.attributes("-fullscreen",True)
    export_data_database()
    window.mainloop()

final()


