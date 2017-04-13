#############################################################
######## K Nearest Neighbors Algorithm for Prediction #######
#############################################################
# - It assumes last column as class attribute
# - first row should be header
# - How to Execute
#   $python k-nearest-neighbors.py <file_name>

# - SAMPLE RUN
#   $ python knn.py knn_data_set.csv 
#   Enter value for k : 3
#   Enter Query value for 'sepal length' : 6.1
#   Enter Query value for 'sepal width' : 2.1
#   Predicted Class Value 'species' : versicolor

import csv
import sys

def euclidean_distance(values, query):
	# Function takes the values , query values and return distance using euclidean distance formula
	# distance(a1, a2, b1, b2) = SQRT((a1-a2)^2 + (b1-b2)^2)
	return sum(map(lambda x: (float(x[0]) - float(x[1]))**2 ,zip(values, query)))**0.5

def find_ditstances(data, query):
	# iterate over data and find euclidean distance of all tuples
	distances = list()
	for index, row in enumerate(data):
		dist = euclidean_distance(row[:-1], query)
		distances.append((index, dist))

	return distances

def readcsv(csv_file):
	# read csv file and return 2 dimentional list and header
	data = list()
	header = list()

	with open(csv_file, 'rb') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		data = list(csvreader)
		header = data[0]
		data = data[1:]
	return header, data

def find_majority(data, k_distances):
	# get k distance values and find majority class value
	class_values_count = dict()
	for index, value in k_distances:
		val = data[index][-1]
		if class_values_count.has_key(val):
			class_values_count[val] += 1
		else:
			class_values_count[val] = 1

	class_value = max(class_values_count.items(), key=lambda x: x[1])[0]
	return class_value


def knn(data, header, k, query):
	# take data, header, k and query values as input
	# use k-nearest-neighbors algorithm to predict class value for query
	
	# find distances of all tuples
	distances = find_ditstances(data, query)
	# find k nearest tuple
	k_min_distances = sorted(distances, key=lambda x: x[1])[:k]
	# predict value by finding majority in k nearest tuples
	predicted_class = find_majority(data, k_min_distances)

	return predicted_class

def main():
	if len(sys.argv)==2:
		header, data = readcsv(sys.argv[1])
	else:
		csv_file_name = raw_input("Enter CSV File Location: ")
		header, data = readcsv("knn_data_set.csv")
	
	parameters, class_name = header[:-1], header[-1]

	k = int(raw_input("Enter value for k : "))

	query = list()
	for param in parameters:
		query.append(float(raw_input("Enter Query value for '%s' : " % param)))

	predicted_class = knn(data, header, 3, query)
	print "Predicted Class Value '%s' : %s " % (class_name, predicted_class)

if __name__ == '__main__':
	main()