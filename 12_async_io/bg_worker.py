import threading
import time
import asyncio

def background_worker():
    while True:
        time.sleep(3)
        print("Logging background work..")

async def fetch_orders():
    await asyncio.sleep(3)
    print("orders fetched")

threading.Thread(target=background_worker, daemon=True).start()
asyncio.run(fetch_orders())