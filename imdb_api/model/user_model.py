from app import db
from entities.user import User, UserTitle
from exceptions.errors import CustomError


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def save(user):
    db.session.add(user)
    db.session.commit()


def get_user_titles(username, args):
    user = get_user_by_username(username)
    user_titles = UserTitle.query.filter_by(user_id=user.id)

    criteria = args.get("criteria")
    if criteria == "watchlist":
        user_titles = user_titles.filter_by(on_watchlist=True)
    elif criteria == "rated":
        user_titles = user_titles.filter(UserTitle.rate > 0)

    if "type" in args:
        user_titles = user_titles.filter(UserTitle.title.type == args.get("type"))

    return user_titles.all()


def create_user_title(user, title):
    ut = UserTitle()
    ut.title = title
    user.titles.append(ut)
    db.session.commit()
    return ut


def get_user_title(user, title):
    user_title = UserTitle.query.filter(
        UserTitle.user_id == user.id, UserTitle.title_id == title.id
    ).first()
    if not user_title:
        user_title = create_user_title(user, title)
    return user_title


def add_title_to_watchlist(user, title):
    user_title = get_user_title(user, title)
    user_title.on_watchlist = True
    db.session.commit()
    return UserTitle.query.filter_by(on_watchlist=True)


def rate_title(title, user, rate):
    user_title = get_user_title(user, title)
    user_title.rate = rate
    db.session.commit()


def remove_title(user, title):
    ut = UserTitle.query.filter_by(title_id=title.id).filter_by(user_id=user.id).get()
    if not ut or not ut.on_watchlist:
        raise CustomError(f"Title {title.id} is not on users watchlist", 400)

    # If the title has not been rated, the association is deleted
    if not ut.rate:
        db.session.delete(ut)
    else:
        ut.on_watchlist = False

    db.session.commit()
    return UserTitle.query.filter_by(on_watchlist=True)


def buy_title(title, user):
    user_title = get_user_title(user, title)
    user_title.purchased = True
    db.session.commit()
