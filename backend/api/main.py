from fastapi import FastAPI
from backend.sniffer.capture import start_capture

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/start")
def start():
    start_capture()
    return {"message": "Sniffing started"}
