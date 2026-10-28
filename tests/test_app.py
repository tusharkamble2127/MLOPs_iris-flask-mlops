import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import app


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200 and r.get_json()["status"] == "ok"


def test_predict_setosa():
    r = app.test_client().post("/predict", json={
        "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2})
    assert r.get_json()["species"] == "setosa"


def test_predict_bad_input():
    r = app.test_client().post("/predict", json={"sepal_length": "x"})
    assert r.status_code == 400


def test_metrics():
    assert b"app_requests_total" in app.test_client().get("/metrics").data
