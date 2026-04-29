from fastapi import FastAPI, Body
import psutil
import random

app = FastAPI()

@app.get("/api/status/")
def api_status():
    return {
        "статус": "ОК",
        "сообщение": "API успешно работает"
    }

@app.get("/api/pc/")
def pc_status():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return {
        "загрузка CPU за 1 сек": cpu,
        "использование RAM": ram,
        "использование диска": disk
    }

@app.get("/api/random-number/")
def random_number():
    a = 0
    b = 99
    return {
        "случайное число": random.randint(a, b)
    }

@app.post("/api/sayhello/")
def say_hello(name: str = Body(..., embed=True)):
    return {
        "приветствие": f"Привет, {name}"
    }