class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        stringArray = text.split()
        numOfWords = len(stringArray)

        for word in stringArray:
            if self.containsAnyCharacter(word, brokenLetters):
                numOfWords = numOfWords - 1

        return numOfWords

    def containsAnyCharacter(self, stringA, stringB):
        """
        :type stringA: str
        :type stringB: str
        :rtype: boolean
        """

        for letter in list(stringB):
            if letter in stringA:
                return True
        
        return False