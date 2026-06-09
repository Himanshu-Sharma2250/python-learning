import threading
import time

def searching_db():
    print("Starts searching db...")
    time.sleep(3)
    print("Finished searching db...")

def writing_in_db():
    print("Starts writing db...")
    time.sleep(5)
    print("Finished writing db...")

t1 = threading.Thread(target=searching_db)
t2 = threading.Thread(target=writing_in_db)

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time taken : {end - start:.2f} seconds")