def solution(answers):
    answer_len = len(answers)
    

    first_pattern = [1,2,3,4,5] 
    second_pattern = [2,1,2,3,2,4,2,5]
    third_pattern = [3,3,1,1,2,2,4,4,5,5] 
    
    first_sheet = []
    second_sheet = []
    third_sheet =[]
    
    first_sheet = (first_pattern) * (answer_len//5) + [first_pattern[i] for i in range(answer_len % 5)]
    second_sheet = (second_pattern) * (answer_len//8) + [second_pattern[i] for i in range(answer_len % 8)]
    third_sheet = (third_pattern) * (answer_len//10) + [third_pattern[i] for i in range(answer_len % 10)]
    
    score_dict = {"first": 0, "second": 0, "third": 0}
    
    for i in range(answer_len):
        if first_sheet[i] == answers[i] : score_dict["first"]+=1 
        if second_sheet[i] == answers[i] : score_dict["second"]+=1    
        if third_sheet[i] == answers[i] : score_dict["third"]+=1 
        
    
    max_score = max(score_dict.values())
    result = []
    
    if score_dict["first"] == max_score : result.append(1)
    if score_dict["second"] == max_score : result.append(2)
    if score_dict["third"] == max_score : result.append(3)

    
    return result