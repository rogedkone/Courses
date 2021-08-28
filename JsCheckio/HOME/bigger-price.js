import assert from "assert";

interface Stock {
    name: string,
    price: number,
};

function biggerPrice(limit: number, data: Stock[]): Stock[] {
    let res = []
    let lastMax = 0
    let lastIdx = 0
    for (let i = 0; i < limit; i++) {
        for (let j = 0; j <= data.length - 1; j++) {
            if (data[j]["price"] > lastMax) {
                lastMax = data[j]["price"]
                lastIdx = j
                }
            }
        res.push(data[lastIdx])
        data.splice(lastIdx, 1)
        lastMax = 0
        }
    return res;
}

console.log('Example:')
console.log(biggerPrice(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))

assert.deepEqual(biggerPrice(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]), [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
])
assert.deepEqual(biggerPrice(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]), [{"name": "whiteboard", "price": 170}])
console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
