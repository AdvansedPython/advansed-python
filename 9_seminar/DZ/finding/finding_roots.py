from decorators import find_roots_from_csv
from decorators import create_json


@create_json
@find_roots_from_csv
def find_roots(a: int = 0,b: int = 0,c: int = 0)->list:
    result = []
    if a == 0:
        if b == 0:
            if c == 0:
                result.append("Бесконечное множество корней")
            else:
                result.append("Корней нет")
        else:
            result.append(f"x = {-c/b}")
        return result

    D = b **2 - 4 * a * c
    if D > 0:
        result.append(f"x1 = {(-b + D**0.5) / (2 * a)}")
        result.append(f"x2 = {(-b - D**0.5) / (2 * a)}")
    elif D < 0:
        result.append("Действительных корней нет")

    else:
        result.append(f"x = {-(b/(2*a))}")

    return result

