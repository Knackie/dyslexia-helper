from unittest.mock import patch
import pytest
from tool.app import correct_text

@pytest.mark.parametrize("input_text, expected_output", [
    ("Il faut que je pars.", "Il faut que je parte."),
    ("Je vais au magazin.", "Je vais au magasin."),
])
def test_correct_text_success(input_text, expected_output):
    """
    Teste une correction réussie avec une réponse simulée de l'API OpenAI.
    """
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.return_value = {
            "choices": [
                {"message": {"content": expected_output}}
            ]
        }
        assert correct_text(input_text) == expected_output

def test_correct_text_missing_api_key():
    """
    Teste le cas où la clé API est absente.
    """
    with patch('os.getenv', return_value=None):
        with pytest.raises(ValueError, match="Clé API OpenAI manquante"):
            correct_text("Texte d'exemple")

def test_correct_text_invalid_api_key():
    """
    Teste le cas où la clé API est invalide.
    """
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.side_effect = openai.error.AuthenticationError("Invalid API key.")
        with pytest.raises(ValueError, match="La clé API est invalide"):
            correct_text("Texte d'exemple")

def test_correct_text_quota_exceeded():
    """
    Teste le cas où le quota est dépassé.
    """
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.side_effect = openai.error.RateLimitError("Quota exceeded.")
        with pytest.raises(ValueError, match="Quota dépassé"):
            correct_text("Texte d'exemple")
