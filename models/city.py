#!/usr/bin/python3
"""Let Define Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represent City class that inherits BaseModel """
    state_id = ""
    name = ""
