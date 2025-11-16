import os


def greet(name: str) -> str:
    return f"Olá, {name}!!!!!!"


if __name__ == "__main__":
    user = os.getenv("APP_USER", "Mundo")
    print(greet(user))
