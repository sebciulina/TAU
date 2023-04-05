class PaymentGateway:
    def process_payment(self, payment_data):
        if not payment_data.get('amount') or not payment_data.get('card_number'):
            return {'error': 'Invalid payment data'}

        card_number = payment_data['card_number']
        if not self._is_valid_card_number(card_number):
            return {'error': 'Invalid card number'}

        amount = payment_data['amount']
        if amount <= 0:
            return {'error': 'Invalid amount'}

        if self._is_fraudulent_transaction(payment_data):
            return {'error': 'Fraudulent transaction detected'}

        return {'success': True}

    def _is_valid_card_number(self, card_number):
        return True


    def _is_fraudulent_transaction(self, payment_data):
        return False
