
global.chrome = {
  storage: {
    local: {
      get: jest.fn((key, callback) => {
        callback({ active: true }); // Mock active state
      }),
      set: jest.fn((data, callback) => {
        callback && callback(); // Mock a successful set
      }),
    },
  },
};
