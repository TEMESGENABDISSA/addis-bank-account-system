from collections import deque


class TransferGraph:
    def __init__(self):
        self.graph = {}

    def add_account(self, account_number):
        if account_number not in self.graph:
            self.graph[account_number] = []

    def add_transfer(self, from_account, to_account):
        self.add_account(from_account)
        self.add_account(to_account)

        self.graph[from_account].append(to_account)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return visited