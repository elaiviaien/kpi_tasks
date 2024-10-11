import asyncio


async def fetch_data():
    try:
        print("Fetching data...")
        await asyncio.sleep(5)
        print("Data fetched!")
    except asyncio.CancelledError:
        print("Fetch cancelled!")


async def main():
    task = asyncio.create_task(fetch_data())

    await asyncio.sleep(2)
    task.cancel()
    await task

if __name__ == "__main__":
    asyncio.run(main())
