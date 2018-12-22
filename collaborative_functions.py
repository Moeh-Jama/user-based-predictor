import statistics 
import math

def getting_mean(ratings):
	number_of_valid_ratings = 0
	sum_of_ratings = 0
	for rating_val in ratings:
		number_of_valid_ratings+=1
		sum_of_ratings += ratings[rating_val]
	return sum_of_ratings/number_of_valid_ratings

def pearsons_correlation(user_j, user_curr):
	#return pearson correaltion and other user id
	top = 0
	#begin multiplying.
	mean_of_j =getting_mean(user_j)
	mean_of_current = getting_mean(user_curr)
	item_index = 1

	bottom = 0
	bottom_left = 0
	bottom_right = 0

	for rated_item in user_curr:
		if rated_item in user_j:
			curr_user_rating = float(user_curr[rated_item])
			user_j_rating = float(user_j[rated_item])
			top += (curr_user_rating - mean_of_current)*(user_j_rating -mean_of_j)
			bottom_left += (curr_user_rating - mean_of_current)**2
			bottom_right+= (user_j_rating - mean_of_j)**2
	item_index =1
	bottom = math.sqrt(bottom_left * bottom_right)

	return top/bottom



def choose_k_best_neighbours(pearson_values, k):
	best_neighbourhood = []
	if k>=len(pearson_values):
		return pearson_values
	for i in range(0,k):
		best_neighbour = pearson_values[0]
		best_index = 0
		index = 0
		for p_vals in pearson_values:
			if p_vals!= None and p_vals[0]!=None and p_vals[-1]!=None:
				if best_neighbour[0]<p_vals[0]:
					best_neighbour = p_vals
					best_index = index
			index+=1
		pearson_values[best_index] = None
		best_neighbourhood.append(best_neighbour)
	return best_neighbourhood

def resnick_algorithm(item_i,users, neighbourhood, required_user):
	#get top
	top = 0
	bottom = 0
	#neighbourhood[i] = [index, p_val]
	for n in neighbourhood:
		pearson_value = n[0]
		user_id = n[-1]
		mean_of_j = getting_mean(users[user_id])
		users_rating_j = int(users[user_id][item_i])
		top+=pearson_value * (users_rating_j - mean_of_j)
		bottom+= abs(pearson_value)

	mean_of_req_user = getting_mean(users[required_user])
	return mean_of_req_user + (top/bottom)