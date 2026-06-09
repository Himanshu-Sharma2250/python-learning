from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Starts brewing {name}")
    time.sleep(2)
    print(f"End brewing {name}")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args={f"taking chai {i+1}"})
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    for p in chai_makers:
        p.join()

    print("Finished all tasks")