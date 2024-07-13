from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for pos, health, dir, idx in robots:
            if dir == 'R':
                stack.append((pos, health, dir, idx))
            else:
                while stack and stack[-1][-2] == 'R' and health > 0:
                    r_pos, r_health, r_dir, r_idx =stack.pop()
                    if r_health > health:
                        r_health -= 1
                        stack.append((r_pos, r_health, r_dir, r_idx))
                        health = 0
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                if health > 0:
                    stack.append((pos, health, dir, idx))
        result = [0] * len(positions)
        for pos, health, dir, idx in stack:
            result[idx] = health
        
        return [h for h in result if h > 0]
    
test = Solution()
print(test.survivedRobotsHealths([1,2,5,6],[10,10,11,11],"RLRL"))