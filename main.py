from fly_in.exceptions import ParsingError
if __name__ == '__main__':
    try:
        raise (ParsingError("I want this"))
    except Exception as e:
        print(e)
