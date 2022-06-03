from calc import VesselVolume

work_on = True

while work_on:
    d_vessel = float(input("Введите диаметр сосуда в мм: \n")) / 1000
    tip = float(input("Введите отношение высота / диаметр: \n"))

    vv = VesselVolume(d_vessel, tip)

    print(vv.volume_calc())