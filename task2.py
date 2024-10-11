import asyncio
import concurrent.futures
from typing import List, Callable

from task1 import async_map, plus_one, multiply_by_two


# --- promise-based alternative ---
async def promise_map(arr: List, func: Callable):
    results = []

    futures = [func(item) for item in arr]

    for future in futures:
        result = await future
        results.append(result)

    return results


def final_callback(result):
    print("Result:", result)


# --- promise-based with parallelism ---

async def promise_map_parallel(arr: List, func: Callable, max_workers: int) -> List:
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        loop = asyncio.get_running_loop()
        tasks = [loop.run_in_executor(executor, lambda: asyncio.run(func(item))) for item in arr]

        for task in asyncio.as_completed(tasks):
            result = await task
            results.append(result)

    return results


# --- running the demos ---
if __name__ == '__main__':
    print("Promise-based Demo case 1:")
    result = asyncio.run(promise_map([1, 2, 3], plus_one))
    print("Result:", result)

    print("Promise-based Demo case 2:")
    result = asyncio.run(promise_map([1, 2, 3], multiply_by_two))
    print("Result:", result)

    print("Async/await Demo case 1:")
    async_map([1, 2, 3], plus_one, final_callback)

    print("Async/await Demo case 2:")
    async_map([1, 2, 3], multiply_by_two, final_callback)

    print("Promise-based with parallelism Demo case 1:")
    result = asyncio.run(promise_map_parallel([1, 2, 3], plus_one, max_workers=2))
    print("Result:", result)

    print("Promise-based with parallelism Demo case 2:")
    result = asyncio.run(promise_map_parallel([1, 2, 3], multiply_by_two, max_workers=2))
    print("Result:", result)
