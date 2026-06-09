from threading import Thread
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order of customer #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai of customer #{i}")
        time.sleep(2)

order_thread = Thread(target=take_orders)
brew_thread = Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

print("All orders taken and chais brewed")