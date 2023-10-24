# Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # False

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in matching:  # if c is an opening bracket
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False

        return not stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)

    def simplifyPath(self, path: str) -> str:
        stack = []
        path_split = path.split('/')

        for c in path_split:
            print(stack)
            if c == '.' or not c:
                continue
            elif c == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)

        return '/' + '/'.join(stack)

    def makeGood(self, s: str) -> str:

        stack = []
        for c in s:
            if len(stack) > 0 and str.lower(stack[-1]) == str.lower(c):
                if (str.isupper(c) and str.islower(stack[-1])) or \
                        (str.isupper(stack[-1]) and str.islower(c)):
                    stack.pop()
                    continue

            stack.append(c)

        return ''.join(stack)



print(Solution().makeGood("s"))
#print(Solution().simplifyPath("/a/./b/../../c/"))
