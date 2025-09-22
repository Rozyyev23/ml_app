from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import pandas as pd
import os
from app.models.model import Model
from app.services.predictor import Predictor

app = FastAPI(title="ML Prediction Service")

templates = Jinja2Templates(directory="app/templates")



model = Model(os.path.join("artifacts", "model.pkl"))

predictor = Predictor(model)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/file")
async def predict_file(request: Request, file: UploadFile):
    df = pd.read_csv(file.file)
    preds = predictor.predict(df)

    # сохраняем результат
    result_df = pd.DataFrame({"id": df.index, "prediction": preds})
    result_df.to_csv("predictions.csv", index=False)

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "filename": "predictions.csv", "predictions": preds.tolist()[:10]},
    )

@app.post("/predict")
async def predict_api(filepath: str = Form(...)):
    df = pd.read_csv(filepath)
    preds = predictor.predict(df)

    result_df = pd.DataFrame({"id": df.index, "prediction": preds})
    result_df.to_csv("predictions.csv", index=False)

    return {"predictions": preds.tolist(), "file": "predictions.csv"}
