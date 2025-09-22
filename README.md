# ML Prediction Service

Сервис на FastAPI для предсказания классов по данным из CSV с использованием обученной модели (model.pkl).


!!! ОБНОВЛЕНО !!!


Предыдущая модель обучена на RandomForest. Так как Ансамбль выводит метрики выше, то я решил попробовать и так оно и есть.
Для интеграции переименуйте файл train_columns.pkl на model.pkl и замените в папке artifacts. На ваше усмотрение. Разница в метриках на 0.1 больше у Ансамбля

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

```python
"predictions": preds.tolist()[:10]
```
на:
```python
"predictions": preds.tolist()
```
## Проверка
```bash
python test.py --student predictions.csv --correct correct_answers.csv
```
