from math import pi
from prettytable import PrettyTable


class VesselVolume:
    def __init__(self, diam, tip):
        self.diam = diam
        self.type = tip

    def volume_calc(self):
        # Расчет высоты емкости
        h_vessel = round(self.type * self.diam, 2)

        # Расчет радиуса емкости
        r_vessel = self.diam / 2

        # Расчет высоты дна сосуда, со средним коэффициэнтом 5
        h_cap = self.diam / 5

        # Расчет объема дна сосуда
        v_cap = (pi * (r_vessel ** 2) * h_cap) * 0.7 * 1000

        # Расчет высоты обечайки сосуда
        h_cyl = h_vessel - 2 * h_cap

        # Расчет объема цилиндра
        v_cyl = pi * (r_vessel ** 2) * h_cyl * 1000

        # Расчет объема емкости
        v_vessel = round(v_cyl + (2 * v_cap), 2)

        # Высота оборудования общая
        h_equip = round(h_vessel * 1.75, 1)

        table = PrettyTable()
        table.add_column("Характеристика",
                         ["Диаметр емкости, м",
                          "Высота сосуда, м",
                          "Объем емкости полный, л",
                          "Общая высота оборудования, м"])
        table.add_column("Значение",
                         [self.diam,
                          h_vessel,
                          v_vessel,
                          h_equip])
        table.align = "l"

        print(table)
        table.clear()
