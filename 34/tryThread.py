import threading

class YurchikMessanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = YurchikMessanger(name='Send out message')
y = YurchikMessanger(name='Receive messages')

y.start()
x.start()
