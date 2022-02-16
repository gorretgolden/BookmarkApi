from flask import Blueprint

bookmarks = Blueprint("bookmarks",__name__)

@bookmarks.get('/new')
def get_all_bookmarks():
    return {'bookmarks':[]}

