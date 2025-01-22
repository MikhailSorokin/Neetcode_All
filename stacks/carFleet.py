class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1 or len(speed) <= 1:
            return min(len(position), len(speed))

        # Sort by tuple position, speed
        zippedList = list(zip(position, speed))
        sortedTuple = list(reversed(sorted(zippedList, key=lambda x : x[0])))
        
        print(sortedTuple)

        prevCarCollided = (target - sortedTuple[0][0]) / sortedTuple[0][1]
        numCarsInFleet = 1
        for i in range(1, len(sortedTuple)):
            currentCarTime = (target - sortedTuple[i][0]) / sortedTuple[i][1] 
            if currentCarTime > prevCarCollided:
                numCarsInFleet += 1
                prevCarCollided = currentCarTime

        return numCarsInFleet