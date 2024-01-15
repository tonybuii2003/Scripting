def removeInvalidParentheses(s: str):
    def dfs(string, current_index, l, r, result):
        nonlocal longest, res
        if current_index >= len(string):
            if l == r:
                if len(result) > longest:
                    longest = len(result)
                    res = set()
                    res.add("".join(result))
                elif len(result) == longest:
                    res.add("".join(result))
        else:
            current_char = string[current_index]
            if current_char == '(':
                result.append(current_char)
                dfs(string, current_index + 1, l + 1, r, result)
                result.pop()
                dfs(string, current_index + 1, l, r, result)
            elif current_char == ')':
                dfs(string, current_index + 1, l, r, result)
                if l > r:
                    result.append(current_char)
                    dfs(string, current_index + 1, l, r + 1, result)
                    result.pop()
            else:
                result.append(current_char)
                dfs(string, current_index + 1, l, r, result)
                result.pop()

    longest = -1
    res = set()
    dfs(s, 0, 0, 0, [])
    return list(res)  # Convert the set to a list before returning

# Call the removeInvalidParentheses function with the input string
input_str = "()())()"
result = removeInvalidParentheses(input_str)
print(result)  # This will print the list of valid strings
