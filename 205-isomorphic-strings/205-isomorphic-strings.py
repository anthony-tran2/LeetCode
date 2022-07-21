class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def map_arr(string):
            hashmap = {
                string[0]: 1
            }
            output = [1]
            counter = 2
            for i in range(1, len(string)):
                char = string[i]
                if char in hashmap:
                    output.append(hashmap[char])
                else:
                    hashmap[char] = counter
                    output.append(counter)
                    counter += 1
            return output
                    
        if map_arr(s) == map_arr(t):
            return True
        return False
        
        