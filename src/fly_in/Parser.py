import re


class Parser:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate(config_file: str) -> None:
        try:
            with open(config_file, "r") as file:

