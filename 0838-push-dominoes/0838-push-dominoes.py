class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = 0
        # add 'L' and 'R' as virtual boundaries to handle
        # cases like '...L' or 'R...' easily.
        final = list('L' + dominoes + 'R')

        for right in range(1, len(final)):
            # only care about non-dot characters
            if final[right] == '.':
                continue
            # found a segment 
            # `left` and `right` are at the boundaries of a segment.
            # `prev` is the character at `final[left]`
            # `next_dom` is the character at `final[right]`
            prev = final[left]
            next_dom = final[right]
            # apply logic to the '.'s *between* left and right.
            # case: R....R -> RRRRRR
            if prev == 'R' and next_dom == 'R':
                for i in range(left + 1, right):
                    final[i] = 'R'
            # case: L....L -> LLLLLL
            elif prev == 'L' and next_dom == 'L':
                 for i in range(left + 1, right):
                    final[i] = 'L'
            # Case: R....L -> RR.LL
            elif prev == 'R' and next_dom == 'L':
                l, r = left + 1, right - 1
                while l < r:
                    final[l] = 'R'
                    final[r] = 'L'
                    l += 1
                    r -= 1
            
            left = right
        return "".join(final[1:-1])


        