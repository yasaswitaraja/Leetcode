class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                st.append('(')
                i += 1
            else:
                # Ensure every closing pair contains two ')'.
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1

                # Match the closing pair with an opening parenthesis.
                if st:
                    st.pop()
                else:
                    ans += 1  # Insert a missing '('.

        # Each unmatched '(' needs two closing parentheses.
        ans += 2 * len(st)

        return ans