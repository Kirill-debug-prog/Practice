distance = int(input("Сколько километров хотите проехать на автомобиле: "))
consumption = int(input("Сколько литров топлива расходует автомобиль на 100 км: "))
tank_capacity = int(input("Сколько литров топлива в вашем баке: "))

fuel_needed = (distance/100) * consumption

if fuel_needed <= tank_capacity:
    print("Вы проедете желаемое расстояние")
else:
    print("У вс недостаточно топлива для поездки на данное расстояние")
