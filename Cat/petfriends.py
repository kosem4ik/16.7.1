
from Cat import Cat


cats = [
    {
        "name": "Барон",
        "gender": "мальчик",
        "age": 2
    },
    {

        "name": "Сэм",
        "gender": "мальчик",
        "age": 2
    }
]

for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))
    print(f'Имя: {cat_obj.name}, '
          f'возраст: {cat_obj.age} года, '
          f'пол: {cat_obj.gender}')
