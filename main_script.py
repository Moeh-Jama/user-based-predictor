import sort_ratings
import collaborative_functions as cf
import random


def random_movie(user_i, movie_list):
	unseen = movies_not_in_user_i(user_i, movie_list)
	return random.choice(unseen)
def random_user(users):
	user_list = []
	for user in users:
		user_list.append(user)
	return random.choice(user_list)
def movies_not_in_user_i(user_i, movie_list):
	unseen_movies = []
	for movie in movie_list:
		if movie[0] not in user_i:
			unseen_movies.append(movie[0])
	return unseen_movies

def pearson_collection(users, item_j, required_user):
	pearson_values = []
	for user in users:
		if item_j in users[user] and user!=required_user:
			pval = cf.pearsons_correlation(users[user], users[required_user])
			pearson_values.append([pval, user]) # add pval
	return pearson_values

def find_movie_name(movie_id, movie_list):
	for movie in movie_list:
		if movie[0]==movie_id:
			return movie[-1]

chosen_user = 1			#Will be replaced with some random userID.
k = 20		#All users selected will have 'item'.
random_unseen_movie = 0	#Will be replaced with some random movieID 'user' has not seen.



user_and_movies = sort_ratings.begin_system()
users = user_and_movies[0]
movie_list = user_and_movies[1]


chosen_user = random_user(users)
random_unseen_movie = random_movie(users[str(chosen_user)], movie_list)
movie_name = find_movie_name(random_unseen_movie, movie_list)
pearson_collection = pearson_collection(users, random_unseen_movie, str(chosen_user))

k_neighbours = cf.choose_k_best_neighbours(pearson_collection, k)

prediction = cf.resnick_algorithm(random_unseen_movie, users, k_neighbours, str(chosen_user))
print('Prediction for item',random_unseen_movie,':',movie_name,'is',prediction,'for user',chosen_user)