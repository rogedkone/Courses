import assert from "assert";

function firstWord(text: string): string {
    let arr_text = text.split(" ")
    let alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (let i of arr_text) {
        if (alpha.includes(i[0])) {
            for (let j = i.length - 1; j >= 0; j--) {
                if (alpha.includes(i[j])) {
                    if (i.includes(".")) {
                        return i.slice(0, i.indexOf("."))
                        } else {
                    return i.slice(0, j + 1)
                        }
                    }
                }
            }
        }
    return "";
}


console.log('Example:')
console.log(firstWord("Hello world"))

// These "asserts" using for self-checking and not for auto-testing
assert.equal(firstWord("Hello world"), "Hello")
assert.equal(firstWord(" a word "), "a")
assert.equal(firstWord("don't touch it"), "don't")
assert.equal(firstWord("greetings, friends"), "greetings")
assert.equal(firstWord("... and so on ..."), "and")
assert.equal(firstWord("hi"), "hi")
console.log("Coding complete? Click 'Check' to earn cool rewards!");
