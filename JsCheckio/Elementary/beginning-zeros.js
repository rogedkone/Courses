import assert from "assert";

function beginningZeros(text: string): number {
    let count = 0
    text.split("")
    for (let i = 0; text[i] == "0"; i++) {
        count += 1
        }
    return count;
}

console.log('Example:');
console.log(beginningZeros('100'));

// These "asserts" are used for self-checking
assert.equal(beginningZeros('100'), 0);
assert.equal(beginningZeros('001'), 2);
assert.equal(beginningZeros('100100'), 0);
assert.equal(beginningZeros('001001'), 2);
assert.equal(beginningZeros('012345679'), 1);
assert.equal(beginningZeros('0000'), 4);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
