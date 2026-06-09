import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    print(f"{name} is Ready.")

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Herbal Chai"),
        brew("Oolong Chai"),
        brew("Ginger Chai"),
        brew("Kali Chai"),
    )

asyncio.run(main())