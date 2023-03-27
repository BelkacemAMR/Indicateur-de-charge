from math import ceil

def battery_charge(percent):
    percent = round(percent)
    num_bars = round(percent / 10)
    print('[' + '❚' * num_bars + ' ' * (10 - num_bars) + ']')
    print(f"{percent}%")

#Test

battery_charge(0)
battery_charge(50)
battery_charge(100)