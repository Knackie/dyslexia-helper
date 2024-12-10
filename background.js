chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.action === "correctText") {
      try {
        const apiKey = "VOTRE_CLE_API"; // Remplacez par votre clé OpenAI
  
        const response = await fetch("https://api.openai.com/v1/completions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
            model: "text-davinci-003",
            prompt: `Corrige les fautes grammaticales et orthographiques dans ce texte : ${message.text}`,
            max_tokens: 100,
          }),
        });
  
        const data = await response.json();
        sendResponse({ correctedText: data.choices[0].text.trim() });
      } catch (error) {
        sendResponse({ error: error.message });
      }
      return true; // Permet une réponse asynchrone
    }
  });
  