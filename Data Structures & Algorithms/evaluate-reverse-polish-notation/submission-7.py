class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        op_tokens = {"+", "-", "/", "*"}
        stack = []

        for token in tokens:
            print(stack)

            if token not in op_tokens:
                stack.append(int(token))
                continue

            second_num = stack.pop()
            first_num = stack.pop()

            if token == "+":
                stack.append(first_num + second_num)
            elif token == "-":
                stack.append(first_num - second_num)
            elif token == "*":
                stack.append(first_num * second_num)
            elif token == "/":
                stack.append(int(first_num / second_num))

        return stack[-1]



        