import threading
import time

def make_chai(chai_type, wait_time:int):
    print(f"{chai_type}. chai_status: Start")
    time.sleep(wait_time)
    print(f"{chai_type}. chai_status: Ready")

t1 = threading.Thread(target=make_chai, args=("Masala Chai", 3))
t2 = threading.Thread(target=make_chai, args=("Kali Chai", 3))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")