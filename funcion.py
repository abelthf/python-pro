# funcion con tipado estático en estructuras de datos de python

from typing import Dict, List, Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    "Argentina": 1,
    "México": 34,
    "Colombia": 45,
}

countries: List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "450000",
    },
    {
        "name": "México",
        "people": "9000000",
    },
    {
        "name": "Colombia",
        "people": "999999999999",
    },
]

print(countries)
