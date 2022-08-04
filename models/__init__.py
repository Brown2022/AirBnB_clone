#!/usr/bin/python3
"""
An __init__ method for the models directory
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
