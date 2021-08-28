import assert from "assert";

function betweenMarkers(text: string, begin: string, end: string): string {
    let beginIdx = text.indexOf(begin)
    let endIdx = text.indexOf(end)
    if (beginIdx < endIdx && beginIdx != -1) {
        return text.slice(beginIdx + begin.length, endIdx)
        }
    else if (endIdx == -1 && beginIdx != -1) {
        return text.slice(beginIdx + begin.length)
        }
    else if (beginIdx == -1 && endIdx != -1) {
        return text.slice(0, endIdx)
        }
    else if (beginIdx > endIdx) {
        return ''
    }
    else {
        return text
        }
}

console.log('Example:')
console.log(betweenMarkers('What is >apple<', '>', '<'), 'apple')

assert.equal(betweenMarkers('What is >apple<', '>', '<'), 'apple')
assert.equal(betweenMarkers("<head><title>My new site</title></head>",
                            "<title>", "</title>"), 'My new site')
assert.equal(betweenMarkers('No[/b] hi', '[b]', '[/b]'), 'No')
assert.equal(betweenMarkers('No [b]hi', '[b]', '[/b]'), 'hi')
assert.equal(betweenMarkers('No hi', '[b]', '[/b]'), 'No hi')
assert.equal(betweenMarkers('No <hi>', '>', '<'), '')
console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
