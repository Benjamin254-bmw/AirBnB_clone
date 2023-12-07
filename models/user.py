#!/usr/bin/python3
""" Let define Class User """

from models.base_model import BaseModel

class User(BaseModel):
    """ Represent Class user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
