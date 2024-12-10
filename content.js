// Charger le dictionnaire
let dictionary = {};

fetch(chrome.runtime.getURL("dictionary.json"))
  .then((response) => response.json())
  .then((data) => {
    dictionary = data;
  });

function isCorrectWord(word) {
  return dictionary.hasOwnProperty(word.toLowerCase());
}

function getSuggestions(word) {
  return Object.keys(dictionary).filter((dictWord) => {
    return dictWord.startsWith(word[0]);
  });
}

function correctText(text) {
  const words = text.split(" ");
  let corrected = "";
  words.forEach((word) => {
    if (!isCorrectWord(word)) {
      const suggestions = getSuggestions(word);
      corrected += suggestions.length > 0 ? suggestions[0] : word;
    } else {
      corrected += word;
    }
    corrected += " ";
  });
  return corrected.trim();
}

chrome.storage.local.get("active", ({ active }) => {
  if (active) {
    document.querySelectorAll("textarea, input[type='text']").forEach((field) => {
      field.addEventListener("input", (event) => {
        const corrected = correctText(event.target.value);
        event.target.value = corrected;
      });
    });
  }
});
