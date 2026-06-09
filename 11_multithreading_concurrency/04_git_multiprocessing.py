from multiprocessing import Process
import time

def crunch_time():
    print("Starting the counting process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Ends the counting process...")

if __name__ == "__main__":
    p1 = Process(target=crunch_time)
    p2 = Process(target=crunch_time)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken in multiprocessing is {end - start:.2f} seconds")