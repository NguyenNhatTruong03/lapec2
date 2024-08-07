from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chào mừng bạn!"}

@app.get("/cong")
def cong(a: float, b: float):
    return {"kết quả": a + b}

@app.get("/tru")
def tru(a: float, b: float):
    return {"kết quả": a - b}

@app.get("/nhan")
def nhan(a: float, b: float):
    return {"kết quả": a * b}

@app.get("/chia")
def chia(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Không thể chia cho 0")
    return {"kết quả": a / b}