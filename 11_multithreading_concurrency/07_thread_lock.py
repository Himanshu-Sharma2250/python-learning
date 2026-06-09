import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    for _ in range(100_000):
        with lock:
            count += 1

threads = [threading.Thread(target=increment) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"Finished counting. Count: {count}")