import time

alarm = input("Set Alarm Time (HH:MM): ")

while True:
    now = time.strftime("%H:%M")
    if now == alarm:
        print ("wake up alarm ringing!")
        break
    time.sleep(30)