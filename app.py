# app.py
def say_hello(name):  # paramètre bien nommé 'name'
    return f"Hello, {name}"  # même orthographe que le paramètre

if __name__ == "__main__":
    print(say_hello("world"))
