
module.exports = {
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"], // Load setup file for mocks
  testEnvironment: "jsdom", // Simulate browser environment
};
