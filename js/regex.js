// see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions

var myRe = new RegExp('orbit ([0-9]+),', 'g');
var matches = myRe.exec('orbit 2, params:');
// matches  ["orbit 2,", "2", index: 0, input: "orbit 2, params:", groups: undefined]