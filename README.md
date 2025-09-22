# ML Prediction Service

Сервис на FastAPI для предсказания классов по данным из CSV с использованием обученной модели (model.pkl).

## Установка
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn app.main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs  
- Веб-интерфейс: http://127.0.0.1:8000/


Загрузка CSV через форму /predict/file

Результат сохраняется в predictions.csv

По умолчанию веб-интерфейс выводит только первые 10 предсказаний.
Чтобы вывести все предсказания, открой app/main.py и в функции predict_file замени:

"predictions": preds.tolist()[:10]

на:
"predictions": preds.tolist()

## Проверка
```bash
python test.py --student predictions.csv --correct correct_answers.csv
```
