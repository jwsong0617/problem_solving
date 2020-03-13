from collections import defaultdict
def solution(genres, plays):
    genres_list = defaultdict(list)
    genres_totalPlays = defaultdict(lambda: 0)
    ret = []
    for i, pair in enumerate(zip(genres, plays)):
        genres_list[pair[0]].append([-pair[1],i])
        genres_totalPlays[pair[0]]+=pair[1]
    for genre in sorted(genres_totalPlays, key=lambda x:genres_totalPlays[x], reverse=True):
        if(len(genres_list[genre])==1):
            ret+=[genres_list[genre][0][1]]
        else:
            sortByPlayNum = sorted(genres_list[genre])[:2]
            ret+=[index for minus_play, index in sortByPlayNum]   
    return ret