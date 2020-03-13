def checkChess(n, impossiblePath_cumulative, rowNum):
    global possibleCases
#     print('\nfunction called')
#     print('rowNum:',rowNum)
    # 기존에 둔 셀을 누적해서 가지고 있는 row를 통해 세로가 겹치거나 대각선이 겹치는 셀을 제거한다
    # 그리하여 현재 row에서 둘 수 있는 포인트를 구함 -> 가능한 셀 구함
    
    # 이미 체스판에 두어진 말들과 비교한다.
    # 가로는 제거할 필요 없음
    # 세로, 대각선만 체크
    curRow = [0]*n
    if(rowNum != 0):
        for rowIdx,colIdx in enumerate(impossiblePath_cumulative):
        #세로 제거
            curRow[colIdx]=1
        #대각선 제거
            diagDiff = rowNum-rowIdx #현재행과 기존 체스말 위치의 차이
            # print('diagDiff:',diagDiff)
            #0일 경우는 없음
            if(diagDiff+colIdx <= n-1): #우하단 대각선
                # print('right down')
                curRow[diagDiff+colIdx]=1
            if(colIdx-diagDiff >= 0): #좌하단 대각선
                # print('left down')
                curRow[colIdx-diagDiff]=1
    if(rowNum == n-1):#맨 마지막 매트릭스면 가능한 포인트들을 구한다.
        #이게 가능한 경우의 수 중 하나
        for element in curRow:
            if(element == 0):
                possibleCases+=1
        possibleList = []
                
    # 다시 리커시브하게 업데이트된 [배치된 체스트 말 리스트]로 checkChess 부름
#     print('curRow:',curRow)
    possibleCols=[i for i, e in enumerate(curRow) if e != 1]
#     print(possibleCols)
#     if(len(possibleCols) != 0):print('possibleCols:',possibleCols) 
    for pIdx in possibleCols:
        impossiblePath = impossiblePath_cumulative[:]
        impossiblePath.append(pIdx)
#         print('impossiblePath:',impossiblePath)
        checkChess(n, impossiblePath, rowNum+1)
    return;

firstLst = []
rowNum = 0
possibleCases=0

def solution(n):    
    # 0이면 가능 1이면 불가능
    checkChess(n,firstLst,rowNum)
    return possibleCases