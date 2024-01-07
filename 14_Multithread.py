from threading import *
from  time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
       def run(self):
           for i in range(5):
                 print("Hi")
                 sleep(1)


t1=Hello()
t2=Hi()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()  #means 'hey main thread wait for t1 and t2 till finish their execution then you'll continue

print('Finished')  # in main thread




