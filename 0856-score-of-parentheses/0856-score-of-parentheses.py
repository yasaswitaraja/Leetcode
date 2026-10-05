class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores = [0]

        for p in s:
            if p == '(':
                scores.append(0)
            else:
                s1 = scores.pop()
                s0 = scores.pop()

                scores.append(max(2 * s1, 1) + s0)

        return scores.pop()