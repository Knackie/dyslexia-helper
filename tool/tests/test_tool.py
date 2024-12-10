from unittest.mock import patch
import pytest
from tool.app import correct_text

# Test : Clé API absente
def test_correct_text_missing_api_key():
    """
    Teste le cas où la clé API est absente.
    """
    with patch('os.getenv', return_value=None):  # Simule l'absence de la clé API
        with pytest.raises(ValueError, match="Clé API OpenAI manquante"):
            correct_text("Texte d'exemple")

# Test : Clé API invalide
def test_correct_text_invalid_api_key():
    """
    Teste le cas où la clé API est invalide.
    """
    import openai  # Assurez-vous que le module est importé dans ce test
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.side_effect = openai.error.AuthenticationError("Invalid API key.")
        with pytest.raises(ValueError, match="La clé API est invalide"):
            correct_text("Texte d'exemple")

# Test : Quota dépassé
def test_correct_text_quota_exceeded():
    """
    Teste le cas où le quota est dépassé.
    """
    import openai  # Assurez-vous que le module est importé dans ce test
    with patch('tool.app.openai.ChatCompletion.create') as mock_create:
        mock_create.side_effect = openai.error.RateLimitError("Quota exceeded.")
        with pytest.raises(ValueError, match="Quota dépassé"):
            correct_text("Texte d'exemple")
