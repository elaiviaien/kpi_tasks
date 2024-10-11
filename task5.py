import asyncio
import heapq
from typing import Callable, List, Tuple


class Observable:
    def __init__(self):
        self._observers: List[Tuple[int, Callable]] = []

    def subscribe(self, observer: Callable, priority: int):
        heapq.heappush(self._observers, (priority, observer))

    def unsubscribe(self, observer: Callable):
        self._observers = [(p, obs) for p, obs in self._observers if obs != observer]
        heapq.heapify(self._observers)

    async def notify(self, *args):
        temp_observers = sorted(self._observers)
        for _, observer in temp_observers:
            await observer(*args)


async def observer1(data):
    await asyncio.sleep(1)
    print(f"Observer 1 received: {data}")


async def observer2(data):
    await asyncio.sleep(0.5)
    print(f"Observer 2 received: {data}")


async def observer3(data):
    await asyncio.sleep(0.8)
    print(f"Observer 3 received: {data}")


async def main():
    observable = Observable()

    observable.subscribe(observer1, priority=2)
    observable.subscribe(observer2, priority=1)
    observable.subscribe(observer3, priority=3)

    await observable.notify("Hello, Observers!")

    await asyncio.sleep(2)

    observable.unsubscribe(observer1)
    await observable.notify("Goodbye, Observers!")


if __name__ == "__main__":
    asyncio.run(main())

