import assert from "assert";

function backwardStringByWord(text: string): string {
    let arrText = text.split(" ")
    let res = ""
    let word = ""
    if (text == "") {
        return text
        }
    else {
        for (let i of arrText) {
            word = ""
            for (let j = i.length - 1; j >= 0; j--) {
                word += i[j]
                }
            res += word + " "
            }
        }
    return res.trim();
}

console.log('Example:');
console.log(backwardStringByWord(''));

// These "asserts" are used for self-checking
assert.equal(backwardStringByWord(''), '');
assert.equal(backwardStringByWord('world'), 'dlrow');
assert.equal(backwardStringByWord('hello world'), 'olleh dlrow');
assert.equal(backwardStringByWord('hello   world'), 'olleh   dlrow');
assert.equal(backwardStringByWord('welcome to a game'), 'emoclew ot a emag');

console.log("Coding complete? Click 'Check' to earn cool rewards!");
