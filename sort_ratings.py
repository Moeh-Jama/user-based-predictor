import csv



system_data = []
def begin_system():
	users = {}
	# Type: users -> users[userID][itemID] = rating for item.
	with open('ratings.csv') as csvFile:
		readCSVFile = csv.reader(csvFile, delimiter=',')
		index = 0
		for row in readCSVFile:
			if index!=0:
				if row[0] not in users:
					users[row[0]] = {}
					users[row[0]][row[1]] = float(row[2])
				else:
					users[row[0]][row[1]] = float(row[2])
			index+=1

	movie_list = []
	with open('movies.csv', encoding="utf8") as csvFile:
		readCSVFile = csv.reader(csvFile, delimiter=',')
		index = 0
		for row in readCSVFile:
			if index!=0:
				movie = []
				movie = [row[0], row[1]]
				movie_list.append(movie)
			index+=1
	return [users,movie_list]

def movies_not_in_user_i(user_i, movie_list):
	for movie in movie_list:
		if movie[0] not in user_i:
			print(movie)	#returns [movieID, movieName]