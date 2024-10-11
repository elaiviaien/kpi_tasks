import asyncio
import time
from typing import Callable, List


# --- demo cases ---

#demo case 1
async def plus_one(item):
    await asyncio.sleep(1)
    return item + 1


# demo case 2
async def multiply_by_two(item):
    await asyncio.sleep(2)
    return item * 2


# --- async map with debounce ---
def async_map(arr: List, func: Callable, final_callback: Callable, debounce_time: float = 0.1):
    results = []

    async def process_item(item):
        start_time = time.time()
        result = await func(item)
        elapsed_time = time.time() - start_time

        if elapsed_time < debounce_time:
            await asyncio.sleep(debounce_time - elapsed_time)

        return result

    async def run():
        nonlocal results
        tasks = [process_item(item) for item in arr]
        results = await asyncio.gather(*tasks)

        final_callback(results)

    asyncio.run(run())


def final_callback(result):
    print("Result:", result)


# --- error handling ---

def async_map_with_error_handling(arr: List, callback: Callable, final_callback: Callable):
    results = []
    errors = []

    async def process_item(item):
        nonlocal errors
        try:
            result = await callback(item)
            return result
        except Exception as e:
            errors.append({"item": item, "error": e})
            return None

    async def run():
        nonlocal results
        tasks = [process_item(item) for item in arr]
        results = await asyncio.gather(*tasks)
        final_callback(results, errors)

    asyncio.run(run())


def final_callback_with_error_handling(result, errors):
    print("Result:", result)
    print("Errors:", errors)


# --- running the demos ---
if __name__ == "__main__":
    print("Demo case 1:")
    async_map([1, 2, 3], plus_one, final_callback)
    print("Demo case 2:")
    async_map([1, 2, 3], multiply_by_two, final_callback)
    print("Demo case 3:")
    async_map_with_error_handling([1, 2, 3], plus_one, final_callback_with_error_handling)
    print("Demo case 4:")
    async_map_with_error_handling([1, 2, 3], multiply_by_two, final_callback_with_error_handling)
