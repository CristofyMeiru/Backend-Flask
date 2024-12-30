from . import user_bp
from flask import jsonify as json

@user_bp.route('/')
def home():
    return json({"message": "Success get user route home!"})