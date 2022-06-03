from math import pi
import termtables as tt


def Vessel_volume(s_thik, d_vessel):  # Толщина стенки и Диаметр емкости в м.
    h_vessel = 1.5 * d_vessel
    print('Общая высота емкости (м)')
    print(round(h_vessel, 2))
    r_vessel = d_vessel / 2
    print('Радиус емкости (м)')
    print(r_vessel)
    h_cap = 3.5 * s_thik + 0.1935 * r_vessel - 0.455 * s_thik
    print('Высота днища (м)')
    print(round(h_cap, 2))
    v_cap = (pi * (r_vessel ** 2) * h_cap) * 0.7 * 1000
    print('Объем днища (л)')
    print(round(v_cap, 2))
    h_cyl = h_vessel - 2 * h_cap
    print('Высота цилиндра (м)')
    print(round(h_cyl, 2))
    v_cyl = pi * (r_vessel ** 2) * h_cyl * 1000
    print('Объем цилиндра (л)')
    print(round(v_cyl, 2))
    v_vessel = v_cyl + 2 * v_cap
    print('Объем емкости (л)')
    print(round(h_cyl, 2))


Vessel_volume(0.04, 0.8)
