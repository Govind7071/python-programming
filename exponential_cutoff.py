import time
i=0
wait_time=1
while i < 5 :
    print("hello world, wait time",wait_time)

    time.sleep(wait_time)
    wait_time*=2
    i+=1