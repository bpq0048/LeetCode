/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    
    let words = text.split(" ");
    let numOfWords = words.length;

    for (let i = 0; i < words.length; i++) {
        if (containsAnyCharacter(words[i], brokenLetters)) numOfWords--; 
    }

    return numOfWords;
};

var containsAnyCharacter = function(stringA, stringB) {
  for (let i = 0; i < stringB.length; i++) {
    if (stringA.includes(stringB[i])) return true;
  }

  return false;
}