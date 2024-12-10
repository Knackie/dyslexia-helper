import os
import openai

# Configurez la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_text(input_text):
    """
    Corrige les fautes grammaticales et orthographiques dans un texte.
    """
    if not openai.api_key:
        raise ValueError("Clé API OpenAI manquante. Définissez la variable d'environnement OPENAI_API_KEY.")

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Corrige les fautes grammaticales et orthographiques dans ce texte : {input_text}",
        max_tokens=100
    )

    corrected_text = response['choices'][0]['text'].strip()
    return corrected_text
