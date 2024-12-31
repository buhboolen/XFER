class Ship:
    def __init__(
        self,
        name: str,
        shipclass: str,
        search: list[str],
        result: list[str],
        url_C: str,
        url_K: str,
        url_M: str,
        url_S: str,
        hulls: list[tuple[str]],
    ):
        self.name = name
        self.shipclass = shipclass
        self.search = search
        self.result = result
        self.url_C = url_C
        self.url_K = url_K
        self.url_M = url_M
        self.url_S = url_S
        self.hulls = hulls

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"SHIP SUMMARY\nNATN:\t{self.nat}\nDESG:\t{self.name}\nCLSS:\t{self.shipclass}\nSOIs:\t{self.search}\nSIGs:\t{self.result}\nURL1:\t{self.url_C}\nURL2:\t{self.url_K}\nURL3:\t{self.url_M}\nURL4:\t{self.url_S}\nHLLS:\t{self.hulls}"

    def summary(self):
        return f"{self.nat} {self.name} {self.shipclass}"

    def whoami(self):
        return type(self).__name__

    def builder(self):
        return f'{self.nat}("{self.name}", "{self.shipclass}", {self.search}, {self.result}, {self.url_C}, {self.url_K}, {self.url_M}, {self.url_S}, {self.hulls}),'


class PRC(Ship):
    def __init__(
        self,
        name: str,
        shipclass: str,
        search: list[str],
        result: list[str],
        url_C: str,
        url_K: str,
        url_M: str,
        url_S: str,
        hulls: list[tuple[str]],
    ):
        super().__init__(name, shipclass, search, result, url_C, url_K, url_M, url_S, hulls)
        self.nat = "PRC"


class RUS(Ship):
    def __init__(
        self,
        name: str,
        shipclass: str,
        search: list[str],
        result: list[str],
        url_C: str,
        url_K: str,
        url_M: str,
        url_S: str,
        hulls: list[tuple[str]],
    ):
        super().__init__(name, shipclass, search, result, url_C, url_K, url_M, url_S, hulls)
        self.nat = "RUS"
		
allships = [
    A := PRC("A", "AA", [1, 2], [2, 1], 9, 8, 7, 6, [(True, True), (False, False)]),
    B := PRC("B", "BB", [1, 2], [2, 1], 9, 8, 7, 6, [(True, True), (False, False)]),
]

for ship in allships:
    print(ship.builder())
