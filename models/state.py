#!/usr/bin/python3
"""
Module for the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""