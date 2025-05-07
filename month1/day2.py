def greet(name):
    return f"Hello, {name}"

print(greet("Jhatleen"))

def add_all(*numbers):
    return sum(numbers)

print(add_all(1,2,3,4))

with open("sample.txt", "w") as f:
    f.write("This is a new file.")

with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)