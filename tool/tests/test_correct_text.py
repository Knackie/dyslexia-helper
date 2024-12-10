import os
import pytest
from tool.app import correct_text

@pytest.mark.parametrize("input_text, expected_output", [
    ("Il faut que je pars.", "Il faut que je parte."),
    ("Je vais au magazin.", "Je vais au magasin."),
    ("Elle a manger la pomme.", "Elle a mangé la pomme."),
    ("Nous avon fini nos devoirs.", "Nous avons fini nos devoirs."),
    ("Vous etes les bienvenus.", "Vous êtes les bienvenus."),
])
def test_correct_text(input_text, expected_output):
    assert correct_text(input_text) == expected_output
