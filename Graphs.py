from collections import defaultdict, deque
from typing import List

from Trees import TreeNode


def build_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        # graph[y].append(x)
        # uncomment the above line if the graph is undirected

    return graph


class SolutionDFS:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                # the next 2 lines are needed to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    print("seen ", i, seen)
                    dfs(neighbor)

        # build the graph
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        print(graph)
        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                # add all nodes of a connected component to the set
                ans += 1
                seen.add(i)
                dfs(i)

        return ans

    def numIslands(self, grid: List[List[str]]) -> int:
        # def dfs(row, col):
        #     # find piece of land in grid == "1"
        #     if 0 <= row < m and 0 <= col < n:
        #         if grid[row][col] == "1" and (row, col) not in seen:
        #             # mark seen
        #             seen.add((row, col))
        #             # find all adjacent pieces of land marking seen ones
        #             for direction in directions:
        #                 dfs(row + direction[0], col + direction[1])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(start_row, start_col):
            stack = [(start_row, start_col)]
            print(1, stack)
            while stack:
                print(2, stack)
                row, col = stack.pop()
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
                        print(3, stack)

        m = len(grid)
        n = len(grid[0])
        seen = set()
        ans = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        # traverse grid
        for row in range(m):
            for col in range(n):
                # find piece of land in grid == "1"
                if grid[row][col] == "1" and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1
                    dfs(row, col)

        # return count of pieces
        return ans

    def numIslands2(self, grid: List[List[str]]) -> int:
        count = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == '1':
                    self.removeNeighbors(r, c, grid)
                    count += 1
        return count

    def removeNeighbors(self, r, c, grid):
        grid[r][c] = 0
        if r + 1 < len(grid) and grid[r + 1][c] == '1':
            self.removeNeighbors(r + 1, c, grid)
        if c + 1 < len(grid[0]) and grid[r][c + 1] == '1':
            self.removeNeighbors(r, c + 1, grid)
        if r - 1 >= 0 and grid[r - 1][c] == '1':
            self.removeNeighbors(r - 1, c, grid)
        if c - 1 >= 0 and grid[r][c - 1] == '1':
            self.removeNeighbors(r, c - 1, grid)

    def visitAllRooms(self, rooms: List[List[int]]) -> bool:
        def exploreRooms(int):
            for key in rooms[int]:
                if key not in available_rooms:
                    available_rooms.add(key)
                    exploreRooms(key)

        # I can open room 0
        available_rooms = set({0})

        # Enter from room 0 to every possible room
        for room, keys in enumerate(rooms):
            exploreRooms(0)

        # do I have keys for each room?
        # compare length of rooms I have access with original number of rooms
        return len(rooms) == len(available_rooms)

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree_list = [0] * n
        # Store indegree of each node
        for _, j in edges:
            indegree_list[j] += 1

        # Look for nodes with indegree == 0
        return [node for node in range(n) if indegree_list[node] == 0]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def exploreNodes(node) -> bool:
            source_found = False
            if node == source:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if not source_found:
                        source_found = exploreNodes(neighbor)
            return source_found

        # Starting from the destination,
        # search every path until reach source
        # Save seen nodes
        seen = set()
        graph = defaultdict(list)

        # build graph
        for i in range(len(edges)):
            node1 = edges[i][0]
            node2 = edges[i][1]
            if node1 == source and node2 == destination or node1 == destination and node2 == source:
                return True
            graph[node1].append(node2)
            graph[node2].append(node1)

        return exploreNodes(destination)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n number of nodes
        # edges[] list of edges between [ai, bi]
        def dfs(node):
            # check if it is not part of seen_nodes set
            if node not in seen_nodes:
                # store seen nodes
                seen_nodes.add(node)
                # check nodes in edges to add in seen_nodes set
                for _ in edges_graph[node]:
                    dfs(_)
            else:
                return

        # create a graph with edges for each node
        edges_graph = defaultdict(list)
        for i in range(len(edges)):
            edges_graph[edges[i][0]].append(edges[i][1])
            edges_graph[edges[i][1]].append(edges[i][0])

        # traverse nodes
        seen_nodes = set()
        count_components = 0
        for i in range(n):
            # check if it is not part of seen_nodes set
            if i not in seen_nodes:
                # add +1 to count_components on every new node
                count_components += 1
                dfs(i)

        return count_components


class SolutionBFS:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen = {(0, 0)}
        queue = deque([(0, 0, 1)])  # row, col, steps
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return -1

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            graph[node].append(node.left)
            graph[node].append(node.right)
            graph[node.left].append(node)
            graph[node.right].append(node)
            dfs(node.right)

        # create undirected graph, so we can access parents and children of target node
        graph = defaultdict(list)
        # use inorder dfs to create graph from root
        dfs(root)
        # store seen nodes
        seen = {target}
        queue = deque([target])
        # search k levels of related nodes from target
        distance = 0
        while queue and distance < k:
            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            distance += 1

        return [node.val for node in queue]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # I have a grid mxn and k number of obstacles (1) I can eliminate
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        # find the minimum number of steps to get from (0,0) to (m-1,n-1)
        # Traverse the grid using BFS, starting point is (0,0)
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        # Directions up (r-1, 0), down (r+1, 0), left (0, c-1), right (0, c+1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, remain, steps = queue.popleft()
            # Stop when arriving to (m-1,n-1)
            if row == m - 1 and col == n - 1:
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col):
                    if grid[next_row][next_col] == 0:
                        seen.add((next_row, next_col, remain))
                        queue.append((next_row, next_col, remain, steps + 1))
                    elif remain and (next_row, next_col, remain - 1) not in seen:
                        seen.add((next_row, next_col, remain - 1))
                        queue.append((next_row, next_col, remain - 1, steps + 1))
        return -1

        # Return number of steps
        # If there's no path return -1

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # n is number of nodes in the graph
        # list of red edges and blue edges
        # return list of the shortest color alternating path
        red = 1
        blue = 0
        # create graph
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[x][red].append(y)

        for x, y in blueEdges:
            graph[x][blue].append(y)

        ans = [float("inf")] * n
        queue = deque([0, 0, red], [0, 0, blue])
        seen = {(0, red), (0, blue)}

        while queue:
            node, steps, color = queue.popleft()
            ans[node] = min(ans[node], steps)
            for neighbor in graph[node][color]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append(neighbor, steps + 1, 1 - color)

        return [x if x != float("inf") else -1 for x in ans]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            # step empty cells only
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        # maze is a list of empty cells (.) and walls (+) mxn
        # entrance is (row, col)
        # exit is an empty cell at the border of the maze

        # find the nearest exit


        # Directions up (r-1, 0), down (r+1, 0), left (0, c-1), right (0, c+1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(maze)
        n = len(maze[0])
        step = 0
        queue = deque([(entrance[0], entrance[1], step)])
        seen = {(entrance[0], entrance[1])}

        while queue:
            row, col, steps = queue.popleft()

            if [row, col] != entrance:
                # return number of steps in the shortest path
                if row == m - 1 or row == 0:
                    return steps
                if col == n - 1 or col == 0:
                    return steps
            else:
                pass
            # traverse grid, can move in directions
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
        # -1 if the path doesn't exist
        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1:])

            return ans

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1


grid = [
    ["0", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "1"],
    ["0", "0", "0", "0", "0"]
]
root = TreeNode(3)
one = TreeNode(5)
two = TreeNode(1)
three = TreeNode(6)
four = TreeNode(2)
five = TreeNode(0)
six = TreeNode(8)
seven = TreeNode(7)
eight = TreeNode(4)

root.left = one
root.right = two
one.left = three
one.right = four
two.left = five
two.right = six
four.left = seven
four.right = eight

print(SolutionBFS().nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1, 0]))
# print(SolutionDFS().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
