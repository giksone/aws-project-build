# test_app.py
from app import say_hello  # Assure-toi que app.py contient bien la fonction say_hello

def test_say_hello():
    # Vérifie que say_hello retourne bien "Hello, AWS" quand on passe "AWS"
    assert say_hello("AWS") == "Hello, AWS"
