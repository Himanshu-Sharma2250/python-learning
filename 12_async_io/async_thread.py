import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Check {item}...")
    time.sleep(3)
    print(f"{item} stock: 3")

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool: 
        result = await loop.run_in_executor(pool, check_stock, "Ginger")
        print(result)

asyncio.run(main())