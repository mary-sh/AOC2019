from pathlib import Path


def calculate_required_fuel(module_mass):
    """
    Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2.
    """
    return int(module_mass / 3.0) - 2


def calculate_fuel_for_fuel(fuel):
    """
    Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.
    However, that fuel also requires fuel, and that fuel requires fuel, and so on.
    Any mass that would require negative fuel should instead be treated as if it requires zero fuel;
    the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside
    the scope of this calculation.
    """
    required_fuel = calculate_required_fuel(fuel)
    return required_fuel + calculate_fuel_for_fuel(required_fuel) if required_fuel > 0 else 0


if __name__ == '__main__':
    required_fuel_total = 0
    fuel_for_fuel_total = 0

    with open(Path('.') / 'data' / 'day_1_input.txt') as f:
        for line in f.readlines():
            required_fuel = calculate_required_fuel(module_mass=int(line))
            required_fuel_total += required_fuel
            fuel_for_fuel_total += calculate_fuel_for_fuel(required_fuel)

    print(required_fuel_total)
    print(required_fuel_total + fuel_for_fuel_total)
