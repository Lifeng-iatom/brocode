import time
def countdown_timer(mytime):
      for countdown in range(mytime,0,-1):
            second = countdown % 60
            minute = int(countdown/60)%60
            hour = int(countdown/3600)
            print(f"{hour:02}:{minute:02}:{second:02}")
            time.sleep(1)

nowtime = int(input("input time in second:"))
countdown_timer(nowtime)
print("time up!")