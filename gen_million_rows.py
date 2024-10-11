# create file with million rows

def generate_file(file_path: str, num_rows: int = 1000000):
    with open(file_path, 'w') as file:
        for i in range(1, num_rows + 1):
            file.write(f"{i}\n")


if __name__ == "__main__":
    num_rows = 1000000
    file_path = "million_rows.txt"
    generate_file(file_path, num_rows)
    print(f"File '{file_path}' with {num_rows} rows generated.")
