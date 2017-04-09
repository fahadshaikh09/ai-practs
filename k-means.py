#############################################################
###############  K Means Clustering Algorithm ###############
#############################################################
# - How to Execute
#   $ python k-means.py
#
# -	sample run
#   $ python k-means.py
#   Enter number of Clusters : 3
#   Enter items (space seprated) : 2 4 6 3 31 12 15 16 38 14 21 23 25 30
#   Clusters : 
#   [2, 4, 6, 3] 3.75
#   [12, 15, 16, 14, 21] 15.6
#   [31, 38, 23, 25, 30] 29.4

def make_clusters(items, mean_values, k):
	# take items and mean values as argument
	# place all items in cluster and return list of clusters

	# empty list to hold clusters 
	clusters = list()
	for i in range(k):
		clusters.append([])
	
	# iterating over items and putting them into cluster
	for i in items:
		cluster_index = select_cluster(i, mean_values)
		clusters[cluster_index].append(i)

	return clusters

def calculate_mean(clusters):
	# calculate mean value of all cluster and return the list of mean values
	return map(lambda cluster: sum(cluster) / float(len(cluster)) if cluster else 0, clusters)

def select_cluster(item, mean_values):
	# take item as argument and choose best cluster for this item
	# returns the index of cluster

	diff = map(lambda x: abs(item-x), mean_values)
	return diff.index(min(diff))

def find_stable_cluster(items, k):
	# take items and number of clusters to be formed

	# initially assume first three values as mean values 
	mean_values = items[:k]
	
	while True:
		# make cluster with given values
		clusters = make_clusters(items, mean_values, k)
		
		# calculate mean values of new cluster
		new_mean = calculate_mean(clusters)

		# if new values are same as last iteration then break
		if new_mean == mean_values:
			break
		# else use these values for next iteration
		mean_values = new_mean
	
	return (clusters, mean_values)
	
def main():
	k = int(raw_input("Enter number of Clusters : "))
	items = raw_input("Enter items (space seprated) : ")
	# split on space and type cast into int
	items = map(lambda i : int(i) , items.split(' '))

	clusters, mean_values = find_stable_cluster(items, k)
	
	print "Clusters : "
	for i in range(len(clusters)):
		print clusters[i], mean_values[i]
	
if __name__=='__main__':
	main()