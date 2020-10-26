from app import app
from flask import request
import json
from validators import validator
from services import payment_service


@app.route("/process_payment", methods=["POST"])
def process_payment():
    """Process a new payment"""
    data = json.loads(request.data)
    validator.validate(data, validator.PAYMENT_DATA)

    payment_service.process_payment(data)

    return "", 200
