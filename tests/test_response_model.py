from api_consumer_project.models.ResponseModel import ResponseModel


def test_response_model_basic():
    resp = ResponseModel(success=True, status_code=200, data={"id": 1})

    assert resp.success is True
    assert resp.status_code == 200
    assert resp.data == {"id": 1}
    assert isinstance(resp.timestamp, str)


def test_response_model_to_dict():
    resp = ResponseModel(success=False, status_code=400, message="Erro")

    d = resp.to_dict()

    assert d["success"] is False
    assert d["status_code"] == 400
    assert d["message"] == "Erro"
    assert "timestamp" in d
