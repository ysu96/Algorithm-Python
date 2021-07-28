def solution(genres, plays):
    answer = []
    kind_genre = {}
    play_genre = {}
    for genre in genres:
        kind_genre[genre] = list()
        # play_genre[genre] = list()
    for i,(genre,play) in enumerate(zip(genres,plays)):
        kind_genre[genre].append((i,play))

    for k in kind_genre:
        play_sum = 0
        for i,play in kind_genre[k]:
            play_sum += play
        play_genre[k] = play_sum

    print(kind_genre)
    print(play_genre)
    while kind_genre:
        max_g = max(play_genre, key=play_genre.get)  # di.get 이용 ->> key를 사용해 value를 얻는 함수
        select = kind_genre[max_g]
        select.sort(key=lambda a: (-a[1], a[0]))

        if len(select) == 1:
            answer.append(select[0][0])
        else:
            answer.append(select[0][0])
            answer.append(select[1][0])
        del kind_genre[max_g]
        del play_genre[max_g]
    # [k for k, v in play_genre.items() if max(play_genre.values()) == v]  -> list comprehension을 이용한 방법


    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))