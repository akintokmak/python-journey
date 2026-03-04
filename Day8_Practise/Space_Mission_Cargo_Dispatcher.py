"""
Senaryo: Bir uzay üssünde lojistik mühendisisin.
Farklı gezegenlere gidecek kargo paketlerinin yakıt maliyetini ve
güvenlik onayını hesaplayan bir sistem kurman gerekiyor.
Her gezegenin uzaklığı ve kargonun ağırlığı farklıdır.
"""

from planet_and_cargo_list import planet_list,cargo_list,dangerous_cargo_list

print("Planets to choose: " + ','.join(planet_list))
print("Cargo to choose  : " + ','.join(cargo_list))
print("Dangerous Cargo to choose: " + ','.join(dangerous_cargo_list))

while True:
    planet_to_choose = input("Planet name: ").title()
    if planet_to_choose not in planet_list:
        print("Please write a correct planet name!")
    else:
        break
while True:
    cargo_type_name = input("Cargo Type: ").title()
    if cargo_type_name not in cargo_list + dangerous_cargo_list:
        print("Please write a correct cargo type!")
    else:
        break

def calculate_fuel(distance,weight,planet_name):
    if planet_name == "Mars":
        fuel = (distance * weight) * 2
    elif planet_name == "Jupiter":
        fuel = (distance * weight) * 5
    else:
        fuel = (distance * weight) * 1.5
    return fuel

def check_mission_safety(fuel_amount,cargo_type):
    if cargo_type in dangerous_cargo_list and fuel_amount > 1200:
        print(f"Mission High Risk! Fuel amount: {fuel_amount}")
    elif cargo_type in cargo_list and fuel_amount > 2500:
        print(f"Mission Medium Risk! Fuel amount: {fuel_amount}")
    else:
        print(f"Mission Acceptable. Fuel amount: {fuel_amount}")

fuel_amount_from_function = calculate_fuel(distance=100,weight=20,planet_name=planet_to_choose)
check_mission_safety(fuel_amount=fuel_amount_from_function,cargo_type=cargo_type_name)


