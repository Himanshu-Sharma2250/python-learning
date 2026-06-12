import threading

chai_stock = 0

def stock_chai():
    global chai_stock
    for _ in range(100_000):
        chai_stock += 1

threads = [threading.Thread(target=stock_chai) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print("chai stocked: ", chai_stock)