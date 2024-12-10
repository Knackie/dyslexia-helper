global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () =>
      Promise.resolve({
        choices: [{ text: "Texte corrigé." }],
      }),
  })
);

const { correctText } = require("../content");

describe("OpenAI API Integration", () => {
  test("correctText should return corrected text", async () => {
    const input = "Texte avec fotes.";
    const corrected = await correctText(input);
    expect(corrected).toBe("Texte corrigé.");
  });
});
