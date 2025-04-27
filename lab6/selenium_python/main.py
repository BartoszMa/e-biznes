from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "secret":
        return {"status": "success"}
    else:
        return {"status": "error", "message": "Invalid credentials"}

@app.get("/products")
def get_products():
    return {"products": ["apple", "banana", "cherry"]}

@app.get("/counter/{number}")
def counter(number: int):
    return {"result": number + 1}

@app.get("/reverse/{text}")
def reverse_string(text: str):
    return {"result": text[::-1]}

@app.get("/status")
def status():
    return {"status": "ok", "uptime": "1234 seconds"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id == 1:
        return {"user": {"id": 1, "name": "Alice"}}
    else:
        return {"error": "User not found"}

@app.get("/uppercase/{text}")
def uppercase(text: str):
    return {"result": text.upper()}

@app.get("/lowercase/{text}")
def lowercase(text: str):
    return {"result": text.lower()}

@app.get("/length/{text}")
def text_length(text: str):
    return {"length": len(text)}

@app.get("/even/{number}")
def is_even(number: int):
    return {"even": number % 2 == 0}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero"}
    return {"result": a / b}

@app.get("/repeat/{word}/{times}")
def repeat(word: str, times: int):
    return {"result": word * times}

@app.get("/palindrome/{word}")
def palindrome(word: str):
    return {"palindrome": word == word[::-1]}

@app.get("/range/{n}")
def generate_range(n: int):
    return {"range": list(range(n+1))}

@app.post("/sum")
def sum_numbers(numbers: list[int]):
    return {"sum.html": sum(numbers)}

@app.get("/day/{n}")
def day_of_week(n: int):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 0 <= n <= 6:
        return {"day": days[n]}
    else:
        return {"error": "Invalid day number"}

@app.post("/reverse-list")
def reverse_list(lst: list):
    return {"reversed": lst[::-1]}

@app.post("/max")
def find_max(numbers: list[int]):
    if not numbers:
        return {"error": "Empty list"}
    return {"max": max(numbers)}

@app.post("/min")
def find_min(numbers: list[int]):
    if not numbers:
        return {"error": "Empty list"}
    return {"min": min(numbers)}

@app.get("/greet/{name}/{role}")
def greet(name: str, role: str):
    return {"message": f"Hello {name}, you are a great {role}!"}
