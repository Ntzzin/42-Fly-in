class FlyInError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(
            "\033[1;91m[Error] \033[0m"
            f"{message}"
        )
