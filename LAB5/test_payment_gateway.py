from unittest.mock import patch
from app import app
import json
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('payment_gateway.PaymentGateway._is_valid_card_number')
@patch('payment_gateway.PaymentGateway._is_fraudulent_transaction')
def test_charge_success(mock_fraudulent, mock_valid, client):
    mock_fraudulent.return_value = False
    mock_valid.return_value = True
    data = {"amount": 100, "card_number": "1234 5678 9012 3456"}
    response = client.post('/payment/charge', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'success': True}

@patch('payment_gateway.PaymentGateway._is_valid_card_number')
@patch('payment_gateway.PaymentGateway._is_fraudulent_transaction')
def test_charge_invalid_card_number(mock_fraudulent, mock_valid, client):
    mock_fraudulent.return_value = False
    mock_valid.return_value = False
    data = {"amount": 100, "card_number": "1234 5678 9012 3456"}
    response = client.post('/payment/charge', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'error': 'Invalid card number'}

@patch('payment_gateway.PaymentGateway._is_valid_card_number')
@patch('payment_gateway.PaymentGateway._is_fraudulent_transaction')
def test_charge_invalid_amount(mock_fraudulent, mock_valid, client):
    mock_fraudulent.return_value = False
    mock_valid.return_value = True
    data = {"amount": -100, "card_number": "1234 5678 9012 3456"}
    response = client.post('/payment/charge', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'error': 'Invalid amount'}

@patch('payment_gateway.PaymentGateway._is_valid_card_number')
@patch('payment_gateway.PaymentGateway._is_fraudulent_transaction')
def test_charge_fraudulent_transaction(mock_fraudulent, mock_valid, client):
    mock_fraudulent.return_value = True
    mock_valid.return_value = True
    data = {"amount": 1000000, "card_number": "1234 5678 9012 3456"}
    response = client.post('/payment/charge', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'error': 'Fraudulent transaction detected'}

