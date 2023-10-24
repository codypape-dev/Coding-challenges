from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) - 1
        left = 0
        while left < right:
            tempChar = s[left]
            s[left] = s[right]
            s[right] = tempChar
            right -= 1
            left += 1

        print(s)

    def sortedSquaresPython(self, nums: List[int]) -> List[int]:

        return sorted(list(map(lambda nm:nm**2,nums)))

    def sortedSquaresAdrian(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        negatives = []
        index = -1
        for i, number in enumerate(nums):
            if (number > 0):
                index = i
                break
            negatives.append(number)
        if (index == 0):
            return list(map(lambda num: num ** 2, nums))
        if index == -1:
            return list(map(lambda num: num ** 2, nums[-1::-1]))
        not_negatives = list(map(lambda num: num * -1, negatives))
        while not_negatives and index < n:
            if not_negatives[-1] < nums[index]:
                arr.append(not_negatives.pop())
            else:
                arr.append(nums[index])
                index += 1
        if index < n:
            arr.extend(nums[index:])
        elif index == n:
            arr.extend(not_negatives[-1::-1])
        return list(map(lambda num: num ** 2, arr))

    def sortedSquaresTwoPointers(self, nums: List[int]) -> List[int]:
        index = -1
        left = 0
        right = len(nums) - 1
        answer = [] * len(nums)

        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                answer.insert(index, nums[left]**2)
                left += 1
                index -= 1
            else:
                answer.insert(index, nums[right]**2)
                right -= 1
                index -= 1
        return answer

def radix(data):
  maximo = max(data)
  unidades = len(str(maximo))
  for unidad in range(1,unidades+1,1):
    counting = [0]*10 #creacion del array
    ordenado = [0]*len(data)
    for dato in data:
      elm = dato%10**unidad - dato%10*(unidad-1)
      elm = int(str(elm)[0])
      counting[elm]+=1
    for i in range(1,len(counting)):
      counting[i]+=counting[i-1]
    for i in range(len(data)-1,-1,-1):
      dato = data[i]
      elm = dato%10**unidad - dato%10*(unidad-1)
      elm = int(str(elm)[0])
      ordenado[counting[elm]-1] = data[i]
      counting[elm]-=1
    for i in range(0,len(data)):
      data[i] = ordenado[i]
  return data

def sortedSquaresRadix(numbers:list[int]) -> list[int]:
    return list(map(lambda num:num**2,radix(list(map(lambda n:abs(n),numbers)))))

print(Solution().reverseString(["h","e","l","l","o"]))
#print(Solution().sortedSquaresTwoPointers([-4,-1,0,3,10]))