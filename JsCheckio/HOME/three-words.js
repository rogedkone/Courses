import assert from "assert";

function threeWords(text: string): boolean {
    let arr_text = text.split(" ").map(Number)
    let count = 0
    for (let i of arr_text) {
        if (isNaN(i)) {
            count += 1
            }
        else {
            count = 0
            }
        if (count == 3) {
            return true;
            }
        }
    return false;
}

console.log('Example:')
console.log(threeWords("Hello World hello"))

assert.equal(threeWords("Hello World hello"), true);
assert.equal(threeWords("He is 123 man"), false);
assert.equal(threeWords("1 2 3 4"), false);
assert.equal(threeWords("bla bla bla bla"), true);
assert.equal(threeWords("Hi"), false);
console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
