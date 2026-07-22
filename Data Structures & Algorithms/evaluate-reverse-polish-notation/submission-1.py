class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}
        stack = []

        for token in tokens:
            if token in operators:
                last_num = stack.pop()
                second_to_last_num = stack.pop()
                
                match token:
                    case "+":
                        stack.append(second_to_last_num + last_num)
                    case "-":
                        stack.append(second_to_last_num - last_num)
                    case "/":
                        stack.append(int(second_to_last_num / last_num))
                    case "*":
                        stack.append(second_to_last_num * last_num)
            else:
                stack.append(int(token))

        return stack.pop()

        