const { isCorrectWord, correctText, getSuggestions } = require('../content');

const mockDictionary = {
  bonjour: true,
  maison: true,
  chat: true,
  chien: true,
  voiture: true,
};

describe('Correcteur Dyslexique Tests', () => {
  test('isCorrectWord should return true for correct words', () => {
    expect(isCorrectWord('bonjour', mockDictionary)).toBe(true);
  });

  test('isCorrectWord should return false for incorrect words', () => {
    expect(isCorrectWord('helo', mockDictionary)).toBe(false);
  });

  test('getSuggestions should suggest correct words', () => {
    const suggestions = getSuggestions('cha', mockDictionary);
    expect(suggestions).toContain('chat');
    expect(suggestions).not.toContain('chien');
  });

  test('correctText should fix incorrect words', () => {
    const input = 'bonjor maison';
    const corrected = correctText(input, mockDictionary);
    expect(corrected).toBe('bonjour maison');
  });
});
