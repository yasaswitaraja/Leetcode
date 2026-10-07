class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        ans = set()

        def is_valid(s):
            balance = 0

            for c in s:
                if c == '(':
                    balance += 1
                    
                elif c == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def backtrack(i, path):
            if i == len(s):
                current = "".join(path)

                if is_valid(current):
                    ans.add(current)

                return

            # Keep the current character
            path.append(s[i])
            backtrack(i + 1, path)
            path.pop()

            # Remove the current character
            if s[i] in "()":
                backtrack(i + 1, path)

        backtrack(0, [])

        max_len = max(map(len, ans))

        return [x for x in ans if len(x) == max_len]
