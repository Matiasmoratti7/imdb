from model import user_model
from entities.user import User
from flask_jwt_extended import create_access_token
from exceptions.errors import CustomError
from config.config import Config
import json, random, datetime, requests
from services.email_service import email_service
from abc import ABC, abstractmethod


def get_user_by_username(username):
    return user_model.get_user_by_username(username)


def get_user_by_id(user_id):
    return user_model.get_user_by_id(user_id)


def register(data):
    user = User(data)
    user_model.save(user)
    return user


def login(data):
    user = get_user_by_username(data.get("username"))
    if not user or not user.check_password(data.get("password")):
        raise CustomError("Wrong user or password", 404)
    expires = datetime.timedelta(days=7)
    return create_access_token(identity=str(user.username), expires_delta=expires)


def is_admin(username):
    user = get_user_by_username(username)
    return user.role == "admin"


def get_user_titles(username, args):
    return user_model.get_user_titles(username, args)


def add_title(username, title):
    user = get_user_by_username(username)
    return user_model.add_title_to_watchlist(user, title)


def rate_title(title, username, rate):
    user = get_user_by_username(username)
    user_model.rate_title(title, user, rate)


def remove_title(username, title):
    user = get_user_by_username(username)
    return user_model.remove_title(user, title)


def buy_title(title, username, data):
    payment_method = data.get("method")
    if payment_method == "credit_card":
        discount_calculator = CCPayment()
    elif payment_method == "paypal":
        discount_calculator = PaypalPayment()
    else:
        raise CustomError("Invalid payment method", 400)

    final_price = discount_calculator.apply_discount(title.price)
    data["total_amount"] = final_price

    payment_response = requests.post(Config.endpoints.process_payment_data, json=data)
    if payment_response.status_code == 400:
        raise CustomError(payment_response.text, 400)

    if payment_response.status_code == 200:
        user = get_user_by_username(username)
        user_model.buy_title(title, user)
        email_service.send_email_to_owner(
            "New sale", f"The customer {username} bought {title.name}", Config.app.owner_email
        )
        email_service.send_email_to_customer(
            "IMDB - Title purchase confirmation",
            f"Congratulations! " f"You have bought {title.name}", data.get("email")
        )
    else:
        raise CustomError("The payment couldn't be processed", 500)


class Payment(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class CCPayment(Payment):
    def apply_discount(self, amount):
        return amount - amount * 10 / 100


class PaypalPayment(Payment):
    def apply_discount(self, amount):
        return amount - amount * (self.get_current_discount()) / 100

    def get_current_discount(self):
        """Simulates asking to Paypal service"""
        return random.randint(0, 100)
