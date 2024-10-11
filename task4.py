# --- general approach ---
import asyncio


def process_line(line: str):
    print(f"Processing: {line.strip()}")


def process_large_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            # file is a generator, so we need to iterate over it
            process_line(line)


# if __name__ == '__main__':
#     file_path = 'million_rows.txt'
#     process_large_file(file_path)

# --- async approach ---
class AsyncLineReader:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.file = None

    def __aiter__(self):
        self.file = open(self.file_path, 'r')
        return self

    async def __anext__(self):
        line = await asyncio.get_event_loop().run_in_executor(None, self.file.readline)

        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopAsyncIteration


async def process_large_file(file_path: str):
    async for line in AsyncLineReader(file_path):
        await asyncio.sleep(0.1)
        print(f"Async processing: {line}")


if __name__ == '__main__':
    file_path = 'million_rows.txt'
    asyncio.run(process_large_file(file_path))
