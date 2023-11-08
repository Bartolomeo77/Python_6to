
import math

users = {
    "Angelica": {
        "Blues Traveler": 3.5,
        "Broken Bells": 2.0,
        "Norah Jones": 4.5,
        "Phoenix": 5.0,
        "Slightly Stoopid": 1.5,
        "The Strokes": 2.5,
        "Vampire Weekend": 2.0,
    },
    "Bill": {
        "Blues Traveler": 2.0,
        "Broken Bells": 3.5,
        "Deadmau5": 4.0,
        "Phoenix": 2.0,
        "Slightly Stoopid": 3.5,
        "Vampire Weekend": 3.0,
    },
    "Chan": {
        "Blues Traveler": 5.0,
        "Broken Bells": 1.0,
        "Deadmau5": 1.0,
        "Norah Jones": 3.0,
        "Phoenix": 5,
        "Slightly Stoopid": 1.0,
    },
    "Dan": {
        "Blues Traveler": 3.0,
        "Broken Bells": 4.0,
        "Deadmau5": 4.5,
        "Phoenix": 3.0,
        "Slightly Stoopid": 4.5,
        "The Strokes": 4.0,
        "Vampire Weekend": 2.0,
    },
    "Hailey": {
        "Broken Bells": 4.0,
        "Deadmau5": 1.0,
        "Norah Jones": 4.0,
        "The Strokes": 4.0,
        "Vampire Weekend": 1.0,
    },
    "Jordyn": {
        "Broken Bells": 4.5,
        "Deadmau5": 4.0,
        "Norah Jones": 5.0,
        "Phoenix": 5.0,
        "Slightly Stoopid": 4.5,
        "The Strokes": 4.0,
        "Vampire Weekend": 4.0,
    },
    "Sam": {
        "Blues Traveler": 5.0,
        "Broken Bells": 2.0,
        "Norah Jones": 3.0,
        "Phoenix": 5.0,
        "Slightly Stoopid": 4.0,
        "The Strokes": 5.0,
    },
    "Veronica": {
        "Blues Traveler": 3.0,
        "Norah Jones": 5.0,
        "Phoenix": 4.0,
        "Slightly Stoopid": 2.5,
        "The Strokes": 3.0,
    },
}
def manhattan(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance 

def euclidean(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += (rating1[key] - rating2[key]) ** 2
    euclidean_distance = math.sqrt(distance)
    return euclidean_distance

def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += x**2
            sum_y2 += y**2
    # if no ratings in common return 0
    if n == 0:
        return 0
    # now compute denominator
    denominator = math.sqrt(sum_x2 - (sum_x*2) / n) * math.sqrt(sum_y2 - (sum_y*2) / n)
        
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


def cosine_similarity(rating1, rating2):
    common_movies = set(rating1.keys()) & set(rating2.keys())
    if not common_movies:
        return 0.0  # No common movies, similarity is 0

    dot_product = sum(rating1[movie] * rating2[movie] for movie in common_movies)
    
    magnitude_rating1 = math.sqrt(sum(rating1[movie] ** 2 for movie in common_movies))
    magnitude_rating2 = math.sqrt(sum(rating2[movie] ** 2 for movie in common_movies))

    if magnitude_rating1 == 0 or magnitude_rating2 == 0:
        return 0.0  # To avoid division by zero
    else:
        return dot_product / (magnitude_rating1 * magnitude_rating2)
    

# Calcular la distancia euclidiana entre 'Hailey' y 'Veronica'
print("-----------")
print(euclidean(users['Angelica'], users['Chan']),)
print("-----------")
print(euclidean(users['Hailey'], users['Jordyn']))
print("-----------")
print(euclidean(users['Hailey'], users['Sam']))
print("-----------")
print(euclidean(users['Veronica'], users['Bill']))
print("-----------")
print("-----------")
print("-----------")
print(manhattan(users['Hailey'], users['Jordyn']))
print("-----------")
print(manhattan(users['Sam'], users['Chan']))
print("-----------")
print(manhattan(users['Dan'], users['Veronica']))
print("-----------")
print(manhattan(users['Angelica'], users['Bill']))
print("-----------")
print("-----------")
print("-----------")
print("-----------")
print(pearson(users['Veronica'], users['Hailey']))
print(cosine_similarity(users['Sam'], users['Bill']))

