import pytest
from unittest.mock import MagicMock, patch

from api_consumer_project.strategies.SoapClient import SoapClient
from api_consumer_project.models.ResponseModel import ResponseModel


def test_soap_client_success() -> None:
    with patch("api_consumer_project.strategies.SoapClient.Client") as mock_client_cls:
        mock_service = MagicMock()
        mock_method = MagicMock(return_value=20)

        mock_service.Add = mock_method
        mock_client_instance = MagicMock()
        mock_client_instance.service = mock_service
        mock_client_cls.return_value = mock_client_instance

        client = SoapClient("http://fake.wsdl")
        response = client.fetch("Add", {"intA": 15, "intB": 5})

        assert isinstance(response, ResponseModel)
        assert response.success is True
        assert response.status_code == 200
        assert response.data == 20
        assert response.message == "SOAP OK"
        mock_method.assert_called_once_with(intA=15, intB=5)

