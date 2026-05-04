class Ota:
    def __init__(self, fullname):
        self.fullname = fullname
        self.__money = 0

    def pul_solish(self, toza_pul):
        pass
        self.__money += toza_pul

    def info(self):
        print(f"Egasi: {self.fullname}")
        print(f"Pull: {self.__money}")
