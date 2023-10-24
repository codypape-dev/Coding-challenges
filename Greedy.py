from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid

        return True

    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1

        return ans

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            if len(heap) == 0:
                # not enough money to do any more projects
                return w

            # minus because we stored negative numbers on the heap
            w -= heapq.heappop(heap)

        return w

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)

        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()
            else:
                break

        return len(ordered)

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        i = 0
        j = len(people) - 1
        people.sort()

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1

            j -= 1
            ans += 1

        return ans

    def maximum69Number(self, num: int) -> int:

        return int(str(num).replace('6', '9', 1))

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes_in_truck = 0
        units_in_truck = 0
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        for i in range(len(boxTypes)):
            if boxes_in_truck + boxTypes[i][0] <= truckSize:
                boxes_in_truck += boxTypes[i][0]
                units_in_truck += boxTypes[i][0] * boxTypes[i][1]
            elif truckSize - boxes_in_truck > 0:
                boxes_to_take = truckSize - boxes_in_truck
                boxes_in_truck += boxes_to_take
                units_in_truck += boxes_to_take * boxTypes[i][1]
                break
        return units_in_truck

print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))