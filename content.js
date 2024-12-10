// Contenu principal pour OpenAI
async function correctText(text) {
  const apiKey = await chrome.storage.local.get("openai_api_key");
  const response = await fetch("https://api.openai.com/v1/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey.openai_api_key}`,
    },
    body: JSON.stringify({
      model: "text-davinci-003",
      prompt: `Corrige les fautes grammaticales et orthographiques dans ce texte: "${text}"`,
      max_tokens: 1000,
    }),
  });

  const data = await response.json();
  return data.choices[0].text.trim();
}

chrome.storage.local.get("active", ({ active }) => {
  if (active) {
    document.querySelectorAll("textarea, input[type='text']").forEach((field) => {
      field.addEventListener("blur", async (event) => {
        const originalText = event.target.value;
        const correctedText = await correctText(originalText);
        event.target.value = correctedText;
      });
    });
  }
});
