def lines(fn):
    try:
        with open(fn, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("File Not found in current directory")
        return []

fn = input()
print(len(lines(fn)))