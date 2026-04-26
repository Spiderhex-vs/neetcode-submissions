class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        nums = []
        for s in tokens:
            if s in operators:
                b = nums.pop()
                a = nums.pop()
                if s == '+':
                    nums.append(a+b)
                elif s == '-':
                    nums.append(a-b)
                elif s == '*':
                    nums.append(a*b)
                else:
                    nums.append(int(a/b))
            else:
                nums.append(int(s))
            
        return nums.pop()
        