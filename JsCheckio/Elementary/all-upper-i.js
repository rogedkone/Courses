import assert from "assert";

function isAllUpper(text: string): boolean {
    let alphabet_low = "abcdefghijklmnopqrstuvwxyz";
    // let alphabet_up = "ABCDEFGHIJKLMOPQRSTUVWXYZ";
    for (let i of text) {
        if (alphabet_low.includes(i)) {
            return false;};
        };
        return true
};

console.log('Example:');
console.log(isAllUpper('ALL UPPER'));

// These "asserts" are used for self-checking
assert.equal(isAllUpper('ALL UPPER'), true);
assert.equal(isAllUpper('all lower'), false);
assert.equal(isAllUpper('mixed UPPER and lower'), false);
assert.equal(isAllUpper(''), true);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
