class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        str_arr = list(s)
        original = False
        while not original:
            str_arr.append(str_arr.pop(0))
            if "".join(str_arr) == goal:
                return True
            if "".join(str_arr) == s:
                original = True
        return False
            
            