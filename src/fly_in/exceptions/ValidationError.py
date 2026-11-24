from .FlyInError import FlyInError


class ValidationError(FlyInError):
    def __init__(self, file: str, line: int, cause: str) -> None:
        super().__init__(
            f"\033[2m{file} on line {line}\033[0m: {cause}"
        )
