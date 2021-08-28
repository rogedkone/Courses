import assert from "assert";

function allTheSame(elements: any[]): boolean {
    let elemLen = elements.length
    if (elemLen < 2) {
        return true}
    else {
        for (let i = 0; i <= elemLen - 2; i++) {
            if (elements[i].toString() === elements[i + 1].toString()) {
                continue
                }
            else {
                return false
                }
            }
        }
    return true;
}


console.log('Example:')
console.log(allTheSame([10000, 99999]))

// These "asserts" are used for self-checking and not for an auto-testing

assert.equal(allTheSame([1, 1, 1]), true)
assert.equal(allTheSame([1, 2, 1]), false)
assert.equal(allTheSame(['a', 'a', 'a']), true)
assert.equal(allTheSame([]), true)
assert.equal(allTheSame([1]), true)
console.log("Coding complete? Click 'Check' to earn cool rewards!");
