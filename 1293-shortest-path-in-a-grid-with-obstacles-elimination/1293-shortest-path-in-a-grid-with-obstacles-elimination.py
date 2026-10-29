class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # scan through grid and map the obstacles
        # count how many obstacles are there
        count_obstacles = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count_obstacles += 1

        # track min dist to travel to (x,y) 
        min_dist = [[[float('inf')] * (count_obstacles + 1) for _ in range(cols)] for _ in range(rows)]
        
        # stated based BFS
        # curr coord, curr dist, # obstacle cleared
        # check theres a obstacle in the beginning
        queue = deque([(0, 0, 0, 0)])
        min_dist[0][0][0] = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            x, y, cur_dist, obstacle_cleared = queue.popleft()

            if x == rows - 1 and y == cols - 1:
                # reached dest
                return cur_dist

            # check neighbors
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy

                # check if neighbor is inbound and if its obstacle, can be eliminated:
                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                    # out of bounds
                    continue

                is_obstacle = (grid[new_x][new_y] == 1)
                # check how many obstacles we cleared so far
                if obstacle_cleared >= min(k, count_obstacles) and is_obstacle:
                    # invalid
                    continue

                # see if we can clear this obstacle
                new_count = obstacle_cleared
                if is_obstacle:
                    new_count = obstacle_cleared + 1

                new_dist = cur_dist + 1
                # only enqueue if we can achieve a smaller dist
                if new_dist < min_dist[new_x][new_y][new_count]:
                    min_dist[new_x][new_y][new_count] = new_dist
                    queue.append((new_x, new_y, new_dist, new_count))

        
        return -1 # we cant clear obstacles under k moves