class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """

        i, j, result = 0, 0, 0

        move, d = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:
                d = (d - 1) % 4
            elif command == -1:
                d = (d + 1) % 4

            else:
                x, y = move[d]

                for k in range(command):
                    if (x + i, y + j) not in obstacles:
                        i += x
                        j += y

                result = max(result, i * i + j * j)

        return result
