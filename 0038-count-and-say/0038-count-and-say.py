class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = "1"

        for _ in range(1, n):
            res = []
            cnt = 1

            for j in range(1, len(s)):
                if s[j] != s[j - 1]:
                    res.append(str(cnt) + s[j - 1])
                    cnt = 1
                else:
                    cnt += 1

            # Add the last group
            res.append(str(cnt) + s[-1])

            s = "".join(res)

        return s