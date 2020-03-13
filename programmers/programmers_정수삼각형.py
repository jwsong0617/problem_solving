def solution(triangle):
    def dp(a,b):        
        if(a==0 and b==0):
            f_data[a][b] = triangle[0][0]
            return f_data[a][b]
        if(f_data[a][b]!=-1):            
            return f_data[a][b]
        if(b==0):            
            f_data[a][b] = triangle[a][b] + dp(a-1,0)            
            return f_data[a][b]
        elif(b==a):
            f_data[a][b] = triangle[a][b] + dp(a-1,b-1)            
            return f_data[a][b]
        else:
            f_data[a][b] =  triangle[a][b] + max(dp(a-1,b-1),dp(a-1,b))            
            return f_data[a][b]

    f_data = [[-1]*(i+1) for i in range(len(triangle))]
    height = len(triangle)
    max_num=0    
    for i in range(height):        
        max_num = max(max_num,dp(height-1,i))    
    return max_num