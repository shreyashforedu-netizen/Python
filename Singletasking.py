from threading import*
from time import*

class Mythread:
    def Work(self):
        print("----Work---")
        task1=input(str("Enter task1"))
        task2=input(str("Enter task2"))
        task3=input(str("Enter task3"))
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("task1")
        sleep(5)
        print("Done")
    
    def task2(self):
        print("task2")
        sleep(5)
        print("Done")    
    
    def task3(self):
        print("task3")
        sleep(5)
        print("Done")    
obj=Mythread()
t1=Thread(target=obj.Work)
t1.start()