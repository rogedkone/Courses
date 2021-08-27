import assert from "assert";

function splitPairs(text: string): string[] {
    let test = []
    let part = ""
    if (text.length % 2 == 0) {
        for (let i = 0; i < text.length; i += 2) {
            part = text[i] + text[i + 1]
            test.push(part)
            }
        return test;
        }
    else {
        for (let i = 0; i < text.length - 1; i += 2) {
        part = text[i] + text[i + 1]
        test.push(part)
            }
            test.push(text[text.length - 1] + "_")
        return test;
        }
}

console.log('Example:');
console.log(splitPairs('abcd'));

// These "asserts" are used for self-checking
assert.deepEqual(splitPairs('abcd'), ['ab', 'cd']);
assert.deepEqual(splitPairs('abc'), ['ab', 'c_']);
assert.deepEqual(splitPairs('abcdf'), ['ab', 'cd', 'f_']);
assert.deepEqual(splitPairs('a'), ['a_']);
assert.deepEqual(splitPairs(''), []);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
