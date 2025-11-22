import pytest
from unittest.mock import patch, MagicMock
from api_consumer_project.strategies.GraphQLClient import GraphQLClient
from api_consumer_project.models.ResponseModel import ResponseModel


@patch("api_consumer_project.strategies.GraphQLClient.requests.post")
def test_graphql_client_success(mock_post) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {"user": {"id": 1, "name": "Alice"}}
    }
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    client = GraphQLClient("https://example.com/graphql")
    params = {"query": "{ user { id name } }"}
    result: ResponseModel = client.fetch(params=params)

    assert result.success is True
    assert result.status_code == 200
    assert result.data == {"data": {"user": {"id": 1, "name": "Alice"}}}
    assert result.message == "GraphQL OK"
    assert result.metadata == {"query": "{ user { id name } }"}

    mock_post.assert_called_once_with(
        "https://example.com/graphql",
        json={"query": "{ user { id name } }"}
    )





