
import sys
import subprocess
try:
    import speedtest
except:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
    'speedtest-cli'])
import time
from datetime import datetime
try:

    import matplotlib
except:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
    'matplotlib'])
import matplotlib.pyplot as plt
count = 0
print("Started the speed logger.")
mins = 5
Times = []
Down = []
Up = []
while 1:
    try:
        print("logging")
        count+=1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f = open('data.txt','a')
        st = speedtest.Speedtest()
        d_st = st.download()//10**6
        u_st = st.upload()//10**6
        Down.append(d_st)
        Up.append(u_st)
        Times.append(count*mins/60)
        plt.plot(Times,Down)
        plt.xlabel("Time [5 min interval]")
        plt.ylabel("Mb/s [Rounded to closest integer]")
        plt.savefig('speed.png')
        s = f"{current_time} : Down speed = {d_st} Mb/s, Up speed = {u_st} Mb/s\n"
        f.write(s)
        f.close()
        print(s)
        if count == 60//mins*24:
            exit
    except:
        i = 0
    time.sleep(mins*60)