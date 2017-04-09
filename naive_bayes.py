#############################################################
###### Naive Bayes Classifier Implementation in Python ######
#############################################################
# - It assumes last column as class attribute
# - first row should be header
# - It uses pandas library, If you haven't installed it execute following command in terminal / CMD to install it
#	pip install pandas
# - How to Execute
#   $ python naive_bayes.py <traing_data_file.csv>

import pandas as np
import sys

def findCount(df, (attrib1, value1), (attrib2, value2)):
	#function takes two attributes with their values and returns count
	return df[(df[attrib1]==value1)&(df[attrib2]==value2)].count()[0]

def naiveBayes(filename, X):
	# function takes two arguments
	# filename is traing data file expected to be in CSV format with first row as header
	# second argument 'X' is question which is suppose to be predicted
	# function assumes the last column as class attribute and returns the predicted class value

	# creating data frame from CSV file
	df = np.read_csv(filename)

	#number of rows in data set
	dataSetLength = len(df)

	#title of class attribute column
	classAttribName = df.columns[-1]
	#class values 
	classValues = tuple(set(df[classAttribName]))

	#class values count
	classAttribValuesCount = dict()
	for value in classValues:
		classAttribValuesCount[value] = df[(df[classAttribName]==value)].count()[0]

	#list of attributes
	attribList = list(df.columns[:-1])

	#propability of class values
	pcValues = dict()
	for i in classValues:
		classValueCount = df[(df[classAttribName]==i)].count()[0]
		pcValues[i] = float(classValueCount)/dataSetLength


	#making empty dictionary with keys as class values
	pciValues=dict()
	for i in classValues:
		pciValues[i] = 1

	#propability of attributes in combination with class values
	for attrib in attribList:
		for classValue in classValues:
			count = findCount(df, (attrib, X[attrib]) , (classAttribName, classValue))
			pciValues[classValue] *=  count / float(classAttribValuesCount[classValue])

	#calculating product of attrib values and class vlaues
	# also find the maximum propabiltiy
	max_value = -1
	max_class = None
	for key, value in pciValues.iteritems():
		tmp = value * pcValues[key]
		if tmp > max_value:
			max_value = tmp
			max_class = key

	return [classAttribName, max_class]

def inputQuestion(filename):
	# function takes filename
	# function allow the user to enter question
	# It returns a dictionary with attributes and values

	df = np.read_csv(filename)
	attribList = list(df.columns[:-1])

	X = dict()

	print "Enter Data to predict (Choose from values given in braces): "
	for attrib in attribList:
		#fetching possible values for attrib
		values = tuple(set(df[attrib]))
		input_question_string = "%s %s : " % (attrib, str(values))
		while True:
			value = raw_input(input_question_string)
			if value in values:
				break
			print "Choose From given values"
		#saving attrib value in dictionary
		X[attrib] = value 

	return X

def main():
	# checking if training data set given using commnad line argument
	# else ask for traing data
	if len(sys.argv) == 2:
		fileName = sys.argv[1]
	else:
		fileName = raw_input("Enter Training Set File Name (CSV) : ")

	X = inputQuestion(fileName)
	print "Given Question : ", X
	predictedClassValue = naiveBayes(fileName, X)
	print "Predicted Class Value for '%s': %s" % (predictedClassValue[0], predictedClassValue[1])

if __name__ == '__main__':
	main()