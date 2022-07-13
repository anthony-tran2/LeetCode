class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(word):
            arr = []
            count = 0
            lastChar = word[0]
            for char in word:
                if lastChar == char:
                    count += 1
                else:
                    arr.append({'char': lastChar, 'count': count})
                    lastChar = char
                    count = 1
            arr.append({'char': lastChar, 'count': count})
            return arr
        
        def test_word(word, arr_test):
            arr_word = compress(word)
            if len(arr_word) != len(arr_test):
                return False
            for i in range(0, len(arr_word)):
                letter1 = arr_word[i]
                letter2 = arr_test[i]
                if letter1['char'] != letter2['char']:
                    return False
                elif letter1['count'] != letter2['count'] and letter1['count'] < 3:
                    return False
                elif letter1['count'] < letter2['count'] and letter1['count'] >= 3:
                    return False
            return True
        
        output = 0
        
        for word in words:
            word_to_test = compress(word)
            if test_word(s, word_to_test):
                output += 1
        return output