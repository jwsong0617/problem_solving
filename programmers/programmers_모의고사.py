def submit(question_nums,answers,submit_pattern):
    correct_num = 0    
    submit_pattern_len = len(submit_pattern)
    for i in range(1,question_nums+1):
        if(i%submit_pattern_len==0):
            if(answers[i-1]==submit_pattern[-1]):
                correct_num+=1            
            continue
        if(submit_pattern[(i%submit_pattern_len)-1]==answers[i-1]):
            correct_num+=1                                
    return correct_num

def solution(answers):
    answer = []
    question_nums = len(answers)
    submit1 = [1,2,3,4,5]
    submit2 = [2,1,2,3,2,4,2,5]
    submit3 = [3,3,1,1,2,2,4,4,5,5]
    s1_num = submit(question_nums,answers,submit1)
    s2_num = submit(question_nums,answers,submit2)
    s3_num = submit(question_nums,answers,submit3)
    answer = [(1,s1_num),(2,s2_num),(3,s3_num)]
    max_correct_num = max(answer, key=lambda x:x[1])[1]    
    answer = [x[0] for x in answer if x[1]==max_correct_num]
    answer.sort()
    return answer