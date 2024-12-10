from unittest.mock import patch
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
    """
    Teste la correction d'un texte en simulant la réponse de l'API OpenAI.
    """
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.return_value = {
            "choices": [
                {"message": {"content": expected_output}}
            ]
        }
        assert correct_text(input_text) == expected_output
