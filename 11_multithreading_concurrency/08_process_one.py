from multiprocessing import Process
import time

def heavy_cpu():
    print("Starts crunching...")
    total = 0
    for _ in range(10**9):
        total += 1
    print("Ends crunching")

if __name__ == "__main__":
    processes = [Process(target=heavy_cpu) for _ in range(2)]

    start = time.time()
    [p.start() for p in processes]
    [p.join() for p in processes]
    end = time.time()

    print(f"Total time taken: {end - start:.2f} seconds")