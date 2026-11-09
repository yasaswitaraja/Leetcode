class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        available = SortedList(range(k))
        busy = []  # (free_time, server_id)

        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have completed their requests
            while busy and busy[0][0] <= arrival[i]:
                free_time, server = heapq.heappop(busy)
                available.add(server)

            # All servers are busy
            if not available:
                continue

            # Find next available server
            start = i % k
            idx = available.bisect_left(start)

            # Wrap around
            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Handle request
            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Return busiest servers
        maxi = max(count)

        return [i for i in range(k) if count[i] == maxi]