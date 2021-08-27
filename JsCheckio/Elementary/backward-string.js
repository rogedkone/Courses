import assert from "assert";

function backwardString(value: string): string {
    let res = "";
    for (let i = 1; value.length - i >= 0; i++) {
        res += value[value.length - i]
        }
    return res;
}

console.log('Example:');
console.log(backwardString('val'));

// These "asserts" are used for self-checking
assert.equal(backwardString('val'), 'lav');
assert.equal(backwardString(''), '');
assert.equal(backwardString('ohho'), 'ohho');
assert.equal(backwardString('123456789'), '987654321');

console.log("Coding complete? Click 'Check' to earn cool rewards!");
