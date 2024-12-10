import os
from unittest.mock import patch
from tool.app import correct_text

@patch("openai.Completion.create")
def test_correct_text(mock_openai):
    """
    Teste la correction d'un texte en simulant la réponse de l'API OpenAI.
    """
    mock_openai.return_value = {
        "choices": [{"text": "Il faut que je parte."}]
    }

    input_text = "Il faut que je pars."
    expected_output = "Il faut que je parte."
    output = correct_text(input_text)

    assert output == expected_output
    mock_openai.assert_called_once()
