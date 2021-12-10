import csv

def begin_system():
	users = {}
	# Type: users -> users[userID][itemID] = rating for item.
	with open('ratings.csv') as csvFile:
		readCSVFile = csv.reader(csvFile, delimiter=',')
		for row in readCSVFile[1:]:
			if row[0] not in users:
				users[row[0]] = {}
				users[row[0]][row[1]] = float(row[2])
			else:
				users[row[0]][row[1]] = float(row[2])

	movie_list = []
	with open('movies.csv', encoding="utf8") as csvFile:
		readCSVFile = csv.reader(csvFile, delimiter=',')
		for row in readCSVFile[1:]:
			movie = []
			movie = [row[0], row[1]]
			movie_list.append(movie)
	return [users,movie_list]
