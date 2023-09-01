class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = []
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                res.append(people[l] + people[r])
                l += 1
                r -= 1  # Decrement the right pointer
            else:
                res.append(people[r])
                r -= 1
        if l == r:
            res.append(people[l])
        return len(res)
