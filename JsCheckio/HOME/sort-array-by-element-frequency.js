import assert from "assert";

function frequencySort(items: any[]): any[] {
    let itemsOne = []
    let temp = []
    let itemsPack = []
    let res = []
    let lastIdx = -1
    for (let i of items) {
        if (!(itemsOne.includes(i))) {
            itemsOne.push(i)
            }
        }
    for (let j of itemsOne) {
        for (let k of items) {
            if (j == k) {
                temp.push(j)
                }
            }
        itemsPack.push(temp)
        temp = []
        }
    for (let g = 0; g < itemsOne.length; g++) {
        for (let h = 0; h < itemsPack.length; h++) {
            if (itemsPack[h].length > temp.length) {
                lastIdx = h
                temp = itemsPack[h]
                }
            }
        res.push(... temp)
        itemsPack.splice(lastIdx, 1)
        temp = []
    }
    
    return res;
}

console.log('Example:');
console.log(frequencySort([4, 6, 2, 2, 6, 4, 4, 4]));

// These "asserts" are used for self-checking and not for an auto-testing
assert.deepEqual(frequencySort([4, 6, 2, 2, 6, 4, 4, 4]), [4, 4, 4, 4, 6, 6, 2, 2]);
assert.deepEqual(frequencySort(['bob', 'bob', 'carl', 'alex', 'bob']), ['bob', 'bob', 'bob', 'carl', 'alex']);
assert.deepEqual(frequencySort([17, 99, 42]), [17, 99, 42]);
assert.deepEqual(frequencySort([]), []);
assert.deepEqual(frequencySort([1]), [1]);


console.log("Coding complete? Click 'Check' to earn cool rewards!");
