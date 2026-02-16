def solution(s):
    s = list(s)
    stack = []
    
    condition = True
    
    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")
        else:
            if len(stack)<=0:
                condition = False
            else:
                if len(stack)>=1:
                    del stack[-1]
                else:
                    condition = False
    
    if len(stack)>=1:
        condition = False         
    
    return condition