class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        if s[0] == "]" or s[0] == "}" or s[0] ==")":
            return False

        for i in range(len(s)):
            if s[i] == '[' or s[i] == "(" or s[i] == '{':
                st.append(s[i])
            else:
                if not st:
                    return False

                if (s[i] == ']' and st[-1] == '[') or (s[i] == '}' and st[-1] == '{') or (s[i] == ')' and st[-1] == '(' ) :
                    st.pop()
                else:
                    return False

        return len(st) == 0