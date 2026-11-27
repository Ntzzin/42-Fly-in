from .Hub import Hub


class Configuration:
    def __init__(self, config_file: str) -> None:
        with open(config_file, "r") as file:
            lines = file.readlines()
        self.__lines: list[str] = lines
        self.nb_drones: int
        self.start_hub: str
        self.end_hub: str
        self.__hubs: list[Hub] = self.__parse_hubs()

    def __parse_hubs(self) -> list[Hub]:
        hub_lines: list[str] = [
            line for line in self.__lines if line.startswith("hub:")
        ]
        hubs: list[Hub] = list()
        for line in hub_lines:
            self.__hubs.append(Hub.from_str(line))
        return hubs

    # def read(self, filename: str) -> None:
    #     with open(filename, "r") as file:
    #         for line_no, line in enumerate(file, start=1):
    #             print(f"{line_no}: {line.rstrip()}")
