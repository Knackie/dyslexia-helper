document.getElementById('activate').addEventListener('click', () => {
  chrome.storage.local.set({ active: true }, () => {
    document.getElementById('status').textContent = 'Statut : Activé';
  });
});

document.getElementById('deactivate').addEventListener('click', () => {
  chrome.storage.local.set({ active: false }, () => {
    document.getElementById('status').textContent = 'Statut : Désactivé';
  });
});
