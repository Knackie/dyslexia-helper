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

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Corrige les fautes grammaticales et orthographiques."},
                {"role": "user", "content": input_text}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.AuthenticationError:
        raise ValueError("La clé API est invalide.")
    except openai.error.RateLimitError:
        raise ValueError("Quota dépassé. Vérifiez vos limites d'utilisation.")
    except openai.error.OpenAIError as e:
        raise ValueError(f"Une erreur OpenAI s'est produite : {e}")
