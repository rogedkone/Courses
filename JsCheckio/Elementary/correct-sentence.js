import assert from "assert";

function correctSentence(text: string): string {
    let res = text[0].toUpperCase() + text.slice(1)
    if (text[text.length - 1] == ".") {
        return res
        } else {
            res += "."
            }
    return res;
}

console.log('Example:');
console.log(correctSentence('greetings, friends'));

// These "asserts" are used for self-checking
assert.equal(correctSentence('greetings, friends'), 'Greetings, friends.');
assert.equal(correctSentence('Greetings, friends'), 'Greetings, friends.');
assert.equal(correctSentence('Greetings, friends.'), 'Greetings, friends.');

console.log("Coding complete? Click 'Check' to earn cool rewards!");
