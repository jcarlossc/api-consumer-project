import pytest
from unittest.mock import patch, MagicMock

from api_consumer_project.core.ApiClientFactory import ApiClientFactory
from api_consumer_project.strategies.RestClient import RestClient
from api_consumer_project.strategies.GraphQLClient import GraphQLClient
from api_consumer_project.strategies.SoapClient import SoapClient
from api_consumer_project.strategies.WebSocketClient import WebSocketClient
from api_consumer_project.strategies.ODataClient import ODataClient


def test_factory_rest():
    client = ApiClientFactory.create("rest", "https://example.com")
    assert isinstance(client, RestClient)


def test_factory_graphql():
    client = ApiClientFactory.create("graphql", "https://example.com/graphql")
    assert isinstance(client, GraphQLClient)


@patch("api_consumer_project.strategies.SoapClient.Client")
def test_factory_soap(mock_zeep_client):

    mock_zeep_client.return_value = MagicMock()
    client = ApiClientFactory.create("soap", "https://fake-wsdl-url.com?wsdl")
    assert isinstance(client, SoapClient)


def test_factory_websocket():
    client = ApiClientFactory.create("websocket", "ws://localhost:8000")
    assert isinstance(client, WebSocketClient)


def test_factory_odata():
    client = ApiClientFactory.create("odata", "https://services.odata.org")
    assert isinstance(client, ODataClient)


def test_factory_case_insensitive():
    client = ApiClientFactory.create("ReSt", "https://example.com")
    assert isinstance(client, RestClient)


def test_factory_invalid_type():
    with pytest.raises(ValueError):
        ApiClientFactory.create("invalid_type", "https://example.com")
