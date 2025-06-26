# simple_debug.py

def greet(name):
    message = f"Hello, {name}!"
    return message  # ← Set a breakpoint here

def main():
    names = ["Alice", "Bob", "Charlie"]
    for idx, person in enumerate(names):
        # ← And here: inspect idx and person
        text = greet(person)
        print(text)
    total = len(names)     # ← Or here: check that total == 3
    print(f"Processed {total} greetings.")

if __name__ == "__main__":
    main()                 
