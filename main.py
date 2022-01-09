# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_dataset(fileName):
    with open(fileName) as file:
        content = file.readlines()
    lab = [line.rstrip() for line in content]
    dicc = {}
    dic = {}
    for j in range(len(lab)):
        a = lab[j]

        b = a.split(",")

        c = b[0]

        for i in range(len(b) - 1):
            d = b[i + 1].split(":")

            f = d[0]

            e = d[1]

            dic[f] = int(e)

            dicc[c] = dic
        dic = {}
    return dicc

def compute_mean_ratings(dict):
    dictt = {}
    sum = 0
    counter = 0
    c = 0
    for users, movies_users_watched in dict.items():
        for movie in movies_users_watched.keys():
            c += 1
            sum = 0
            counter = 0
            for key, value in dict.items():
                if value and movie in value.keys():
                    sum += value[movie]
                    counter += 1
            avg = sum / counter
            dictt[movie] = avg
        avg = 0
    return dictt

def find_most_similar_users(dic, id, n):
    dictt = compute_mean_ratings(dic)
    di = {}
    dic_similarities = {}
    for users_ in dic.keys():
        total = 0.0001
        sim = 0
        for movies_ in dic[id]:

            if movies_ in dic[users_]:
                a = (dic[id][movies_] - dic[users_][movies_])
                a = abs(a)
                di[movies_] = a
                total += a
            else:
                a = dic[id][movies_] - dictt[movies_]
                a = abs(a)
                total += a

        for moviess in dic[users_]:
            if not moviess in dic[id]:
                difference = (dic[users_][moviess] - dictt[moviess])
                difference = abs(difference)
                total += difference

        sim = 1 / total
        dic_similarities[users_] = sim

    sort_dic_sim = sorted(dic_similarities.items(), key=lambda x: x[1], reverse=True)
    similars = {}

    for number in range(n + 1):
        similars[number] = sort_dic_sim[number][0]

    liste = []
    for add in similars.values():
        liste.append(add)

    return liste

def make_recommendations(dic, sim_users):
    liste = []
    ref_user = sim_users[0]
    sim_users.remove(ref_user)
    for user in sim_users:
        for a, b in dic[user].items():
            if b > 2:
                liste.append(a)

    for movies in dic[ref_user].keys():
        if movies in liste:
            liste.remove(movies)

    return liste

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

#
def abs(v):
    return v if v > 0 else -v


#
#
user_id, N = input().split(',')
N = int(N)
rating_histories = read_dataset('ratings.csv')
mean_ratings = compute_mean_ratings(rating_histories)
most_similar_ids = find_most_similar_users(rating_histories, user_id, N)
movies = make_recommendations(rating_histories, most_similar_ids)
print(','.join(sorted(list(set(movies)))))
#
