from http import HTTPStatus

from fastapi.testclient import TestClient

from first_fast_api.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização do teste)

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    # Estrutura de como o dicionário trafega na rede
    assert response.json() == {'mensagem': 'te amo luli'}
