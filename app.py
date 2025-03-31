from fastapi import FastAPI
from pydantic import BaseModel
from sentiment import analyze_sentiment
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.post("/analyze")
def sentiment_endpoint(request: TextRequest):
    result = analyze_sentiment(request.text)
    return result

app.mount("/", StaticFiles(directory=".", html=True), name="static")
