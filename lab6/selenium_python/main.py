from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

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

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/index.html", response_class=HTMLResponse)
def serve_homepage():
    with open(os.path.join("static", "index.html")) as f:
        return f.read()

@app.get("/counter.html", response_class=HTMLResponse)
def serve_counter():
    with open(os.path.join("static", "counter.html")) as f:
        return f.read()

@app.get("/day.html", response_class=HTMLResponse)
def serve_day():
    with open(os.path.join("static", "day.html")) as f:
        return f.read()

@app.get("/dayofweek.html", response_class=HTMLResponse)
def serve_day_week():
    with open(os.path.join("static", "dayofweek.html")) as f:
        return f.read()

@app.get("/divide.html", response_class=HTMLResponse)
def serve_divide():
    with open(os.path.join("static", "divide.html")) as f:
        return f.read()

@app.get("/even.html", response_class=HTMLResponse)
def serve_even():
    with open(os.path.join("static", "even.html")) as f:
        return f.read()

@app.get("/factorial.html", response_class=HTMLResponse)
def serve_factorial():
    with open(os.path.join("static", "factorial.html")) as f:
        return f.read()

@app.get("/greet.html", response_class=HTMLResponse)
def serve_greet():
    with open(os.path.join("static", "greet.html")) as f:
        return f.read()

@app.get("/hello.html", response_class=HTMLResponse)
def serve_hello():
    with open(os.path.join("static", "hello.html")) as f:
        return f.read()

@app.get("/length.html", response_class=HTMLResponse)
def serve_length():
    with open(os.path.join("static", "length.html")) as f:
        return f.read()

@app.get("/login.html", response_class=HTMLResponse)
def serve_login():
    with open(os.path.join("static", "login.html")) as f:
        return f.read()

@app.get("/lowercase.html", response_class=HTMLResponse)
def serve_lowercase():
    with open(os.path.join("static", "lowercase.html")) as f:
        return f.read()

@app.get("/max.html", response_class=HTMLResponse)
def serve_max():
    with open(os.path.join("static", "max.html")) as f:
        return f.read()

@app.get("/min.html", response_class=HTMLResponse)
def serve_min():
    with open(os.path.join("static", "min.html")) as f:
        return f.read()

@app.get("/multiply.html", response_class=HTMLResponse)
def serve_multiply():
    with open(os.path.join("static", "multiply.html")) as f:
        return f.read()

@app.get("/nowtime.html", response_class=HTMLResponse)
def serve_nowtime():
    with open(os.path.join("static", "nowtime.html")) as f:
        return f.read()

@app.get("/odd.html", response_class=HTMLResponse)
def serve_odd():
    with open(os.path.join("static", "odd.html")) as f:
        return f.read()

@app.get("/palindrome.html", response_class=HTMLResponse)
def serve_palindrome():
    with open(os.path.join("static", "palindrome.html")) as f:
        return f.read()

@app.get("/prime.html", response_class=HTMLResponse)
def serve_prime():
    with open(os.path.join("static", "prime.html")) as f:
        return f.read()

@app.get("/products.html", response_class=HTMLResponse)
def serve_products():
    with open(os.path.join("static", "products.html")) as f:
        return f.read()

@app.get("/random.html", response_class=HTMLResponse)
def serve_random():
    with open(os.path.join("static", "random.html")) as f:
        return f.read()

@app.get("/range.html", response_class=HTMLResponse)
def serve_range():
    with open(os.path.join("static", "range.html")) as f:
        return f.read()

@app.get("/repeat.html", response_class=HTMLResponse)
def serve_repeat():
    with open(os.path.join("static", "repeat.html")) as f:
        return f.read()

@app.get("/reverse.html", response_class=HTMLResponse)
def serve_reverse():
    with open(os.path.join("static", "reverse.html")) as f:
        return f.read()

@app.get("/reverse-list.html", response_class=HTMLResponse)
def serve_reverse_list():
    with open(os.path.join("static", "reverse-list.html")) as f:
        return f.read()

@app.get("/status.html", response_class=HTMLResponse)
def serve_status():
    with open(os.path.join("static", "status.html")) as f:
        return f.read()

@app.get("/sum.html", response_class=HTMLResponse)
def serve_sum():
    with open(os.path.join("static", "sum.html")) as f:
        return f.read()

@app.get("/uppercase.html", response_class=HTMLResponse)
def serve_uppercase():
    with open(os.path.join("static", "uppercase.html")) as f:
        return f.read()

@app.get("/user.html", response_class=HTMLResponse)
def serve_user():
    with open(os.path.join("static", "user.html")) as f:
        return f.read()

@app.get("/uuid.html", response_class=HTMLResponse)
def serve_uuid():
    with open(os.path.join("static", "uuid.html")) as f:
        return f.read()
