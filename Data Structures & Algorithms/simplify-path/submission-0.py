class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        cur = ''

        for i in path+'/':
            if i == '/':
                if cur =='..':
                    if st:
                        st.pop()
                elif cur != "" and cur != '.':
                    st.append(cur)
                cur = ''
            else:
                cur += i

        return '/' + '/'.join(st)