
test('Chrome API mock works', () => {
  chrome.storage.local.get("active", ({ active }) => {
    expect(active).toBe(true);
  });

  chrome.storage.local.set({ active: false }, () => {
    expect(chrome.storage.local.set).toHaveBeenCalledWith(
      { active: false },
      expect.any(Function)
    );
  });
});
