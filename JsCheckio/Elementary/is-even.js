import assert from "assert";

function isEven(num: number): boolean {
    return (num % 2 == 0);
}

console.log('Example:');
console.log(isEven(2));

// These "asserts" are used for self-checking
assert.equal(isEven(2), true);
assert.equal(isEven(5), false);
assert.equal(isEven(0), true);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
