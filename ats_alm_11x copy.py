import network
from machine import Pin       # เพิ่มเข้ามาทดสอบ
import time
from linelib import tiny_line

#--Innitial #1 -------------
wlan_ssid = "DANGMCOT 2.4GHz"
wlan_password = "21436587"

wlan = network.WLAN(network.STA_IF)
#---------------------------------
led0 = Pin(2,Pin.OUT)

switch1x = Pin(26,Pin.IN)  # GPIO26  pin12 สีเหลือง
switch2x = Pin(34,Pin.IN)  # GPIO34  pin10 สีเขียว
switch3x = Pin(32,Pin.IN)  # GPIO32  pin8  สีเทา

led1 = Pin(13,Pin.OUT)     # GPIO13  pin16 display
led2 = Pin(15,Pin.OUT)     # GPIO13  pin22 display
led3 = Pin(33,Pin.OUT)     # GPIO33  pin7  display
led11 = Pin(2,Pin.OUT)     # GPIO2   led ในบอร์ดฯ

led3.value(0)
led11.value(1)
time.sleep(0.5)
led3.value(1)
led11.value(0)
time.sleep(0.5)
led3.value(0)
led11.value(1)
time.sleep(0.5)
led3.value(1)
led11.value(0)  

led1.value(1)
led2.value(1)
led3.value(1)
#---
wlan.active(True)
time.sleep(0.5)
wlan.connect(wlan_ssid,wlan_password)
time.sleep(5)    # เดิม = 10 วินาที
#---
#access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'

access_token = 'kBinA2n9QvPLPFzTpI5Xrkv6zbXDJBFS0aVo0NLRzhh'
message = tiny_line(access_token)
message.notify("สน.หัวหิน:ระบบแจ้งเตือนไฟฟ้าทำงาน")

time.sleep(10)

#--Innitial #2 -------------
def wlan_connect():
    wlan.active(True)
    time.sleep(0.5)
    wlan.connect(wlan_ssid,wlan_password)
    time.sleep(10)
    #-------------
#----++++++++++------+++++++++++++---------+++++--
#------------------------------------
def MainProg_1():                  #1 ("สน.หัวหิน:ไฟฟ้าปกติ_Gen.ทำงาน")
    time.sleep_ms(1000)
    led1.value(1)
    time.sleep_ms(10)
    if switch1x.value() == 0:              #1  เช็ค sw.1 เป็นหลัก ปกติ  1 ทำงาน
        time.sleep_ms(10)
        if switch2x.value() == 0:          #1  เช็ค sw.2 เป็นหลัก ปกติ  1 ทำงาน
            led2.value(0)                  # display
            led1.value(1)                  # led F.F.
            wlan_connect()                 # คำสั่ง connect wifi 
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าปกติ_Gen.ทำงาน")   # ปกติ2  
            time.sleep_ms(555)    # เดิม 500ms
            #-----------------------------------------------------
            #--เรียก loop check load ---
            time.sleep_ms(555)    # เดิม 500ms
            check_load()
            time.sleep_ms(555)    # เดิม 500ms
            #--จบการเช็คโหลด-------------
            #led3.value(0)     # test+++start+++++++++++++++++++++++++++++++++++++++++
            #-------------------------------
            #--ดีเลย์ชุดนี้..เพื่อตั้งช่วงเวลาบอกว่าไฟฟ้าปกติทุกๆ 5-6 นาที/ครั้ง และ out loop ได้..
            #--
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            #check_load()       # เช็ค load ซ้ำ
            #-----------------------
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01x()     # deldy 1 นาที แบบมี sensor ภายใน
            
            #led3.value(1)     # test+++start+++++++++++++++++++++++++++++++++++++++++
            #--
        time.sleep_ms(10) 
    #----------------------------------------------------------------
    #-- +++++++++++------+++++++      # ("สน.หัวหิน:ไฟฟ้าขัดข้อง_Genไม่ทำงาน")  
    if switch1x.value() == 1:              #0 เช็ค sw.1 เป็นหลัก ปกติ  0 ทำงาน
        time.sleep_ms(10)
        if switch2x.value() == 1:          #0 เช็ค sw.2 เป็นหลัก ปกติ  0 ทำงาน
            led2.value(0)                  # display
            led1.value(1)                  # led F.F.
            wlan_connect()                 # คำสั่ง connect wifi 
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าขัดข้อง_Genไม่ทำงาน")   # ปกติ2
            time.sleep_ms(555)    # เดิม 500ms
            #-----------------------------------------------------
            #--เรียก loop check load ---
            time.sleep_ms(555)    # เดิม 500ms
            check_load()
            time.sleep_ms(555)    # เดิม 500ms
            #--จบการเช็คโหลด-------------
            #-------------------------------
            #--ดีเลย์ชุดนี้..เพื่อตั้งช่วงเวลาบอกว่าไฟฟ้าปกติทกๆ 5-10 นาที/ครั้ง และ out loop ได้..
            #--
            time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #check_load()
            time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            
            #time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #time_delay_01m()     # deldy 1 นาที แบบมี sensor ภายใน
            #--
        time.sleep_ms(10)
    #------------------
    #-- +++++++++++------+++++++      # ("สน.หัวหิน:ไฟฟ้าขัดข้อง_Gen.ทำงานปกติ")      
    if switch1x.value() == 1:              #0 เช็ค sw.1 เป็นหลัก ปกติ  0 ทำงาน
        time.sleep_ms(10)
        if switch2x.value() == 0:          #1 เช็ค sw.2 เป็นหลัก ปกติ  1 ทำงาน
            led2.value(0)                  # display
            led1.value(1)                  # led F.F.
            wlan_connect()                 # คำสั่ง connect wifi 
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าขัดข้อง_Gen.ทำงานปกติ")  # ปกติ2 
            time.sleep_ms(555)     # เดิม 500ms
            #-----------------------------------------------------
            #--เรียก loop check load ---
            time.sleep_ms(555)     # เดิม 500ms
            check_load()
            time.sleep_ms(555)     # เดิม 500ms
            #--จบการเช็คโหลด-------------
            #--------------------------------
            #--ดีเลย์ชุดนี้..เพื่อตั้งช่วงเวลาบอกว่าไฟฟ้าปกติทกๆ 30 นาที/ครั้ง และ out loop ได้..
            #led3.value(0)     # test+++start+++++++++++++++++++++++++++++++++++++++++
            #--
            time_delay_01g()        # deldy  1 นาที แบบมี sensor ภายใน
            #-
            #check_load()
            #--
            #time_delay_01g()   #ใช้จริง ลบ ออก
            #time_delay_01g()   #ใช้จริง ลบ ออก
            #time_delay_01g()   #ใช้จริง ลบ ออก
            #------------------------------
            #led3.value(0)     # test+++start+++++++++++++++++++++++++++++++++++++++++
            if switch1x.value() == 1:   #0
                time_delay_01gg()       # deldy 10 นาที แบบมี sensor ภายใน
            time.sleep_ms(1)      
            if switch1x.value() == 1:   #0   
                time_delay_01gg()       # deldy 10 นาที แบบมี sensor ภายใน
            time.sleep_ms(1)      
            if switch1x.value() == 1:   #0
                time_delay_01gg()       # deldy 10 นาที แบบมี sensor ภายใน
            time.sleep_ms(1)
            if switch1x.value() == 0:   #1
                time.sleep_ms(1)
            time.sleep_ms(1)
            #--
            #led3.value(1)     # test+++stop+++++++++++++++++++++++++++++++++++++++++
        time.sleep_ms(1) 
    #-----------------------------
    #-- +++++++++++------+++++++  +---+++++++ # ("สน.หัวหิน:ไฟฟ้าปกติ")     
    if switch1x.value() == 0:       #1 เช็ค sw.1 เป็นหลัก ,ไฟฟ้าปกติ  1 ลูบนี้ทำงาน
        time.sleep_ms(10)
        if switch2x.value() == 1:   #0 เช็ค sw.2 เป็นหลัก ,gen. ดับ  0 ลูบนี้ทำงาน
            led2.value(0)                     # display
            led1.value(1)                     # led F.F.
            wlan_connect()                    # คำสั่ง connect wifi
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าปกติ")     # ปกติ1
            time.sleep_ms(555)      # เดิม 500ms
            #-----------------------------------------------------            
            #--เรียก loop check load ---
            time.sleep_ms(555)      # เดิม 500ms
            check_load()
            time.sleep_ms(555)      # เดิม 500ms 
            #--จบการเช็คโหลด-------------         
            #-------------------------------
        #--ดีเลย์ชุดนี้..เพื่อตั้งช่วงเวลาบอกว่าไฟฟ้าปกติทกๆ 1ชม. 10นาที/ครั้ง และ out loop ได้..
            #------------------------ตลอดเวลาเมื่อไฟฟ้าดับ และไฟฟ้าไม่ดับ Gen.ทำงาน..
            #time_delay_00t()     # deldy  1 นาที แบบมี sensor ภายใน(ไม่ใช้)
            #time_delay_00t()     # deldy  1 นาที แบบมี sensor ภายใน(ไม่ใช้)
            #time_delay_00t()     # deldy  1 นาที แบบมี sensor ภายใน (ไม่ใช้)
            #time_delay_00t()     # deldy  1 นาที แบบมี sensor ภายใน (ไม่ใช้)
            #time_delay_00t()     # deldy  1 นาที แบบมี sensor ภายใน(ไม่ใช้)
            #----------
            time_delay_58()       # deldy 58 นาที แบบมี sensor ภายใน (ใช้)
            #--
            time_delay_05h()      # deldy 5 ชั่วโมง แบบมี sensor ภายใน (ใช้)
            #---รวมค่า delay  =  6 ชม.---(เพิ่มได้ตามต้องการ)
            led3.value(0)     # test+++start++++++++++++++++++++++++++++++++
            time.sleep(2)         #debug
            led3.value(1)     # test+++start++++++++++++++++++++++++++++++++
            #-----------------------------------------------------
            led1.value(1)     
        led1.value(1)        
    #------------------
    time.sleep_ms(1000)
    led1.value(0)           # led สีส้ม
    led2.value(1)           # led สีน้ำเงิน
    
    return  MainProg_1()    # Debug แก้ปัญหา++++++55555555555 ได้ผล...ครั้งล่าสุด..
#-- จบ loop โปรแกรมหลัก ----------------------
#----------------------------------------------------------------
#/////////////////////////////////////////////////////////////// 
#-----------------------------------------------------------------------    
#---ลูปเช็ค Load--ทำงานแจ้งครั้งแรกหากไฟฟ้า load หาย(ส่งวน)หรือ load กลับมาส่งเพียงครั้งเดียว--
#-- Delay + Sensor Load ว่าไฟฟ้าจ่ายได้ปกติ หรือไม่ ---
#--
def check_load():  
    if switch3x.value() == 1:            #0 เช็ค#1 sw.3 ปกติ 0 ทำงาน , 1 หลุด
        time.sleep_ms(10)
        if switch3x.value() == 1:        #0 เช็ค#2 sw.3 ปกติ 0 ทำงาน , 1 หลุด
            led2.value(0)                # display 
            led1.value(1)                # led F.F.
            wlan_connect()               # คำสั่ง connect wifi 
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าไม่จ่าย load ดับ ")
            time.sleep_ms(500)
        time.sleep_ms(10) 
    #------------------
        
    if switch3x.value() == 0:              #1 เช็ค sw.3 ปกติ 1 ทำงาน , 0 หลุด
        time.sleep_ms(10)
        if switch3x.value() == 0:          #1 เช็ค sw.3 ปกติ 1 ทำงาน , 0 หลุด
            led2.value(0)                  # display
            led1.value(1)                  # led F.F.
            wlan_connect()                 # คำสั่ง connect wifi 
            # คำสั่ง เรียกเข้าระบบ Line
            access_token = 'PYmUKG4c7EFdMpm7fsvXVR9YsbMHEahdiaZAK8eq4JA'
            time.sleep_ms(10)
            message = tiny_line(access_token) # คำสั่งเรียก message
            message.notify("สน.หัวหิน:ไฟฟ้าจ่าย load ปกติ")   # "ได้ปกติ"
            time.sleep_ms(500)
        time.sleep_ms(10)
    time.sleep_ms(10)
    #---จบการเช็คโหลด-----
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
#-----------------------------------------------------------------
#---ใช้งานต่อจากคำสั่ง ----  "สน.หัวหิน:ไฟฟ้าปกติ_Gen.ไม่ทำงาน") ------    
#---------------โชว์คำว่า--("สน.หัวหิน:ไฟฟ้าปกติ") ------------
    
def delay_ss3_1():
    if switch1x.value() == 0:       #1 เช็ค sw.1 เป็นหลัก ปกติ  1 ทำงาน
        for i in range(1000):
            time.sleep_ms(1)
    if switch1x.value() == 1:       #0 เช็ค sw.1 เป็นหลัก ปกติ  0 หลุด
        time.sleep_ms(1)
    time.sleep_ms(1)
    #--------------
def time_delay_00():                # รวม = 5 นาที
    for i in range(150):      
        delay_ss3_1()
        led2.value(0)
        led3.value(1)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        delay_ss3_1()
        led2.value(1)
        led3.value(0)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        if switch2x.value() == 0:   #1   ..+ กับเช็ค sw.2 ปกติ 0 ถ้า 1 หลุด----
            MainProg_1()
        time.sleep_ms(10)
        #--- 
#--------------------------    
def time_delay_00t():               # รวม = 1 นาที
    for i in range(30):      
        delay_ss3_1()
        led2.value(0)
        led3.value(1)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        delay_ss3_1()
        led2.value(1)
        led3.value(0)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        if switch2x.value() == 0:   #1   ..+ กับเช็ค sw.2 ปกติ 0 ถ้า 1 หลุด----
            MainProg_1()
        time.sleep_ms(10)
        #---
def time_delay_08():            # รวม = 08 นาที
    if switch1x.value() == 0:    #1   ที่จริง 3 นาที..แต่ทดบาดเจ็บมา 5 นาทีแล้ว   
        time_delay_00t()
        time_delay_00t()
        time_delay_00t()
    time.sleep_ms(1)
    #--
    time_delay_00()
    #---------
def time_delay_58():                # รวม = 50 นาที
    if switch1x.value() == 0:     #1
        #time_delay_08()  # 8 min # ถอดออก..เพราะทดบาดเจ็บ 3 นาที พอดี
        time_delay_00t()        #  1 min
        time_delay_00t()        #  1 min
        time_delay_00t()        #  1 min
        time_delay_00t()        #  1 min
        #--
        time_delay_01()         # 10 min
        time_delay_01()         # 10 min
        time_delay_01()         # 10 min  
        time_delay_01()         # 10 min 
        time_delay_01()         # 10 min
    time.sleep_ms(1)    
    #--
#-------------------
def time_delay_01():                # รวม = 10 นาที
    if switch1x.value() == 0:     #1
        time_delay_00()    
        time_delay_00()
    time.sleep_ms(1)    
    #---------
def time_delay_01h():               # รวม = 1  ชั่วโมง
    if switch1x.value() == 0:     #1
        time_delay_01()
        time_delay_01()
        time_delay_01()
        time_delay_01()
        time_delay_01()
        time_delay_01()
    time.sleep_ms(1)    
    #-----------------
def time_delay_05h():               # รวม = 5  ชั่วโมง
    if switch1x.value() == 0:     #1
        time_delay_01h()    
        time_delay_01h()
        time_delay_01h()
        time_delay_01h()
        time_delay_01h()
    time.sleep_ms(1)
    #-------------------
#-------------------------------------
    
#---------------------------------------------------------
#---ใช้งานต่อจากคำสั่ง ----  "สน.หัวหิน:ไฟฟ้าปกติ_Gen.ทำงาน") ------
    #---------------
def delay_ss3_2():
    if switch2x.value() == 0:       #1   เช็ค sw.2 เป็นหลัก ปกติ  1 ทำงาน
        for i in range(500):
            time.sleep_ms(1)
    if switch2x.value() == 1:       #0   เช็ค sw.2 เป็นหลัก ปกติ  0 หลุด
        time.sleep_ms(1)
    time.sleep_ms(1)
    #---------------
def time_delay_00x():               # = 1 นาที
    for i in range(60):      
        delay_ss3_2()
        led2.value(0)
        led3.value(1)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        delay_ss3_2()
        led2.value(1)
        led3.value(0)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        if switch1x.value() == 1:   #0   ..+ กับเช็ค sw.1 ปกติ 1 ถ้า 0 หลุด 
            MainProg_1()
        time.sleep_ms(1)            # เดิม 100 
        #------------   
def time_delay_01x():               # รวม = 1 นาที
    if switch2x.value() == 0:     #1
        time_delay_00x()
    time.sleep_ms(1)    
    #time_delay_00x()
#-------------------------------------
#---------------------------------------------------------------
    
#---------------------------------------------------------------
#---ใช้งานต่อจากคำสั่ง ----("สน.หัวหิน:ไฟฟ้าขัดข้อง_Gen.ทำงานปกติ")--------
def delay_ss3_22():
    if switch1x.value() == 1:       #0    เช็ค sw.1 เป็นหลัก ปกติ  0 ทำงาน
        for i in range(500):
            time.sleep_ms(1)
    if switch1x.value() == 0:       #1    เช็ค sw.1 เป็นหลัก ปกติ  1 ทำงาน
        time.sleep_ms(1)
    time.sleep_ms(1) 
    #--------------
def time_delay_00g():               # = 1 นาที
    #if switch1x.value() == 0:  # test.........ทดลอง พร้อมลบออก-----------       
    for i in range(60):     
        delay_ss3_22()
        led2.value(0)
        led3.value(1)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        delay_ss3_22()
        led2.value(1)
        led3.value(0)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        if switch2x.value() == 1:   #0   ..+ กับเช็ค sw.2 ปกติ 1 ถ้า 0 หลุด ,ปกติ sw.2x
            MainProg_1()
        time.sleep_ms(10)      # เดิม 100
        #---
    time.sleep_ms(1)    
    #------------ --  
def time_delay_01g():               # รวม =  1 นาที
    if switch1x.value() == 1:   #0    ------พร้อม ลบออก-----new  -----------new
        time_delay_00g()
    time.sleep_ms(1)
    #--------------
def time_delay_01gg():              #      รวม = 10 นาที
    if switch1x.value() == 1:   #0
        for i in range(10):
            time_delay_00g() 
        time.sleep_ms(1)
    time.sleep_ms(1)
 #-------------------------   
#--------------------------
    
#--------------------------------------------------------------
#---ใช้งานต่อจากคำสั่ง ----("สน.หัวหิน:ไฟฟ้าขัดข้อง_Genไม่ทำงาน")----ok
def delay_ss3_11():
    if switch1x.value() == 1:       #0   เช็ค sw.1 เป็นหลัก ปกติ  0 ทำงาน
        for i in range(500):
            time.sleep_ms(1)
    if switch1x.value() == 0:       #1   เช็ค sw.1 เป็นหลัก ปกติ  1 หลุด
        time.sleep_ms(1)
    time.sleep_ms(1)    
    #--------------- 
def time_delay_00m():               # = 1 นาที
    for i in range(60):          
        delay_ss3_11()
        led2.value(0)
        led3.value(1)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        delay_ss3_11()
        led2.value(1)
        led3.value(0)    # ใช้เป็น clock กระตุ้นเพื่อ reset cpu เมื่อแฮ้งค์ไม่เกิน2นาที
        if switch2x.value() == 0:   #1    ..+ กับเช็ค sw.2 ปกติ 0 ถ้า 1 หลุด
            MainProg_1()
        time.sleep_ms(10)           #  ค่าเดิม 100 msec
        #---
    #------------   
def time_delay_01m():               # ลูปใช้งาน รวม = 1 นาที
    time_delay_00m()    
    #time_delay_00m()   
#------------------------- ------------------------------------    
   
    
#--------------------------------------------------------------   
#--------------------------------------------------------------
    
while True:
    MainProg_1()
    
#----------------
#--------------------------------------------------------------
    
    
    
    
    
    
    
    