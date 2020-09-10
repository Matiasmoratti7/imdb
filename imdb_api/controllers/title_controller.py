from model import title_model


def get_title_by_id(title_id):
    return title_model.get_title_by_id(title_id)


def get_titles(args):
    return title_model.get_titles(args)
