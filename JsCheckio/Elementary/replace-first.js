import assert from "assert";

function replaceFirst(values: number[]): number[] {
    if (values.length < 2) {
        return values;
        }
    else {
        values.push(values[0])
        values.shift()
        return values;
        }
}

console.log('Example:');
console.log(replaceFirst([1, 2, 3, 4]));

// These "asserts" are used for self-checking
assert.deepEqual(replaceFirst([1, 2, 3, 4]), [2, 3, 4, 1]);
assert.deepEqual(replaceFirst([1]), [1]);
assert.deepEqual(replaceFirst([]), []);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
