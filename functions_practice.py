def hello():
    print("Hello, user!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        for i, item in enumerate(lunch_items):
            if i == 0:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")

# Example usage:
hello()

lunchbox = pack('sandwich', 'apple', 'cookie')
eat_lunch(lunchbox)
