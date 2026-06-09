import threading
import time

def monitoring_chai_temp():
    while True:
        print("Monitoring chai temperature...")
        time.sleep(2)

t = threading.Thread(target=monitoring_chai_temp) # monitor function keeps on running
t.start()

print("Main program done")