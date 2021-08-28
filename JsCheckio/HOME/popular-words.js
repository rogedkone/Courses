"use strict";

function popularWords(text: string, words: string[]) {
    let textArr = text.toLowerCase().split("\n").join(" ").split(" ");
    let count = 0
    let res = {}
    for (let i of words) {
        count = 0
        for (let j of textArr) {
            if (i == j) {
                count += 1
                }
            };
        res[i] = count;
        };
    return res;
}


console.log('Example:')
console.log(popularWords(`
When I was One
I had just begun
When I was Two
I was nearly new`, ['i', 'was', 'three', 'near']))
