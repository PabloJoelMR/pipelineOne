const assert = require('assert');
const main = require('./main');

describe('TestMainFunction', function() {
  it('test_main', function() {
    assert.strictEqual(main(null), "Hello World!");
  });
});