class KelasKursus:
    def __init__(self):
        self.__kuota = 5  # private

    def daftar(self):
        if self.__kuota > 0:
            self.__kuota -= 1