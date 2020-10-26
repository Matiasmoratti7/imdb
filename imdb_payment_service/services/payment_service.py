from exceptions.errors import CustomError


def process_payment(data):
    payment_method = data.get("method")

    payment_data = {"total_amount": data.get("total_amount")}
    if payment_method == "credit_card":
        payment_data.update(
            {
                key: value
                for (key, value) in data.items()
                if key in ["cvv", "card_holder", "cc_number"]
            }
        )
        credit_card_gateway(data)
    elif payment_method == "paypal":
        payment_data["paypal_acount"] = data.get("paypal_account")
        paypal_gateway(data)
    else:
        raise CustomError("Invalid payment method", 400)


def credit_card_gateway(data):
    """Simulates the contact with the defined credit card gateway"""
    pass


def paypal_gateway(data):
    """Simulates the contact with paypal gateway"""
    pass
