document.body.addEventListener("mouseup", () => {
  const selection = window.getSelection().toString();
  if (selection) {
    chrome.runtime.sendMessage(
      { action: "correctText", text: selection },
      (response) => {
        if (response.correctedText) {
          alert(`Texte corrigé : ${response.correctedText}`);
        } else if (response.error) {
          console.error("Erreur :", response.error);
        }
      }
    );
  }
});
