
# Iris FastAPI — Iris Flower Prediction API

Lightweight FastAPI service that predicts Iris flower species from sepal/petal measurements using a pre-trained scikit-learn model.

**Project layout**
- `app/` — FastAPI application code (routes, Pydantic schemas).
- `model/` — trained model artifact (`iris_model.joblib`) and training script.
- `env/` — optional local virtualenv (not committed normally).
- `Dockerfile`, `docker-compose.yml` — containerization files.
- `load_test.py` — simple load test script.

## Requirements
- Python 3.11+ (virtual environment recommended)
- See `requirements.txt` for exact packages.

## Quick setup (local)
1. Create and activate a virtual environment (Windows example):

```bash
python -m venv env
env\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API (development):

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 7860
```

The API will be available at `http://127.0.0.1:7860` and interactive docs at `http://127.0.0.1:7860/docs`.

## API Endpoints

- `GET /health` — health check. Returns `{"status":"ok"}`.
- `GET /info` — model metadata (model type, feature names, classes).
- `POST /predict` — predict species. Accepts JSON with numeric measurements and returns predicted class.

Example request to `/predict`:

```bash
curl -X POST "http://127.0.0.1:7860/predict" \
	-H "Content-Type: application/json" \
	-d '{"sepal_length":5.1, "sepal_width":3.5, "petal_length":1.4, "petal_width":0.2}'
```

Example JSON schema (see `app/schemas.py`):

```json
{
	"sepal_length": 5.1,
	"sepal_width": 3.5,
	"petal_length": 1.4,
	"petal_width": 0.2
}
```

Response:

```json
{
	"predicted_class": "setosa"
}
```

## Model training

A training script is provided at `model/train_model.py`. It trains a scikit-learn model and writes `model/iris_model.joblib` which the API loads at startup.

To retrain and save a new model:

```bash
python model/train_model.py
```

## Docker

Build image:

```bash
docker build -t iris-fastapi .
```

Run with docker-compose:

```bash
docker-compose up --build
```

This exposes the service on the port configured in `docker-compose.yml` (default `7860`).

## Load testing

The repository includes `load_test.py` for simple throughput checks. Adjust parameters inside the script and run:

```bash
python load_test.py
```

## Notes
- The API expects the model artifact at `model/iris_model.joblib` — replace if retraining.
- Pydantic schemas validate input types; invalid payloads return 422 errors.

## Contributing
- Open an issue or submit a PR with improvements.

## License
This project is provided as-is for educational purposes. Replace with a proper license if used in production.
