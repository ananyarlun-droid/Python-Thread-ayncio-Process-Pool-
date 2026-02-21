import asyncio

async def job(name, sec):
    print(f"Start job {name}")
    await asyncio.sleep(sec)
    print(f"Done job {name}")
    return name

async def main():
    tasks = [
        job("A", 2),
        job("B", 3),
        job("C", 1),
    ]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

await main()
