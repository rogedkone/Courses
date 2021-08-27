import assert from "assert";

function nearestValue(values: number[], search: number): number {
    let profit = 9999;
    let res = 0;
    values = values.sort(function(a, b){return a - b})
    for (let i of values) {
        if (Math.abs(search - i) < profit) {
            profit = Math.abs(search - i)
            res = i;
        };
    };
    return res;
}

console.log('Example:');
console.log(nearestValue([4, 7, 10, 11, 12, 17], 9));

// These "asserts" are used for self-checking
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 9), 10);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 8), 7);
assert.equal(nearestValue([4, 8, 10, 11, 12, 17], 9), 8);
assert.equal(nearestValue([4, 9, 10, 11, 12, 17], 9), 9);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 0), 4);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 100), 17);
assert.equal(nearestValue([5, 10, 8, 12, 89, 100], 7), 8);
assert.equal(nearestValue([-1, 2, 3], 0), -1);

console.log("Coding complete? Click 'Check' to earn cool rewards!");
