document.getElementById("correctText").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;
  
    chrome.runtime.sendMessage({ action: "correctText", text: inputText }, (response) => {
      if (response.error) {
        alert("Erreur : " + response.error);
      } else {
        document.getElementById("outputText").value = response.correctedText;
      }
    });
  });
  