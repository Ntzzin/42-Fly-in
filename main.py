from src.fly_in.exceptions import *

if __name__ == '__main__':
    try:
        raise (ValidationError("main.py", 3, "I want this"))
    except Exception as e:
        print(e)
