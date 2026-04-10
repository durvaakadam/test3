def user_info(name: str, age: int):
    return {
        "name": name,
        "age": age,
        "is_adult": age >= 18
    }
