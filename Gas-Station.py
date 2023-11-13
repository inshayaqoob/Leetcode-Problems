class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        if sum(cost) > sum(gas):
            return -1
        for i in  range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i +1
            
        return start