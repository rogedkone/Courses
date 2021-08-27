import assert from "assert";

function endZeros(value: number): number {
    let count = 0;
    let i = 0;
    let str_value = value.toString()
    while (str_value.length != i) {
        if (str_value[str_value.length - (i + 1)] === "0") {
            count += 1
            i += 1
            } else {
                break
                };
        }
    return count;
};

console.log('Example:');
console.log(endZeros(0));

// These "asserts" are used for self-checking
assert.equal(endZeros(0), 1);
assert.equal(endZeros(1), 0);
assert.equal(endZeros(10), 1);
assert.equal(endZeros(101), 0);
assert.equal(endZeros(245), 0);
assert.equal(endZeros(100100), 2);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
