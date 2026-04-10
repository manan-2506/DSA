class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for i in tokens:
            res = 0
            if i == "+" or i == "*" or i == "-" or i == "/":
                a = st[-1]
                st.pop()
                b = st[-1]
                st.pop()
                if i =="+":
                    res = a+b
                elif i =="-":
                    res = b-a
                elif i =="*":
                    res = a*b
                elif i =="/":
                    res = int(b/a)
                
                st.append(res)
            else:
                st.append(int(i))

        return st[-1]