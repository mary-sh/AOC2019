from pathlib import Path


def calculate_required_fuel(module_mass):
    """
    Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
    take its mass, divide by three, round down, and subtract 2.

    For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed
    for the mass of each module (your puzzle input), then add together all the fuel values.

    What is the sum of the fuel requirements for all of the modules on your spacecraft?
    """
    return int(module_mass / 3.0) - 2


def calculate_fuel_for_fuel(fuel):
    """
    Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.
    However, that fuel also requires fuel, and that fuel requires fuel, and so on.
    Any mass that would require negative fuel should instead be treated as if it requires zero fuel;
    the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside
    the scope of this calculation.

    So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you
    just calculated as the input mass and repeat the process,
    continuing until a fuel requirement is zero or negative.

    For example:

    A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
    which would call for a negative fuel), so the total fuel required is still just 2.

    At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
    216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel,
    which requires no further fuel. So, the total fuel required for a module of mass 1969 is
    654 + 216 + 70 + 21 + 5 = 966.

    The fuel required by a module of mass 100756 and its fuel is:
    33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
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
