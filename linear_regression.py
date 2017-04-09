#############################################################
#################### Linear Regression ######################
#############################################################
# - CSV file is assume to have cleaned data with header
# - It is assumed that first column is dependent variable and second column is independent variable
# - How to Run
#   $ python linear_regression.py <training_data.csv>
#
# -	sample run
#   $ python linear_regression.py liner_regression_sample_data.csv 
#   Equation :  3.7 + 1.46x
#   Enter value of x : 5
#   Predicted Value of y :  11.0
#   Enter value of x : 10
#   Predicted Value of y :  18.3

import pandas as pd
import sys

class LinearRegression():

	def __init__(self, csvFile):
		self.df = pd.read_csv(csvFile)
		self.calculteCoefficient()

	def calculteCoefficient(self):
		df = self.df

		num, den = 0, 0
		xmean = df.ix[:,0].mean()
		ymean = df.ix[:,1].mean()

		for i in range(0, len(df)):
			num += ((df.ix[:,0][i] - xmean) * (df.ix[:,1][i]-ymean))
			den += (df.ix[:,0][i]-xmean)**2

		self.b1 = num/den
		self.b0 = float(ymean- self.b1*xmean)

	def predict(self, x):
		return (self.b0 + self.b1*x)

	def getEquation(self):
		return "%s + %sx" % (self.b0, self.b1)
		
def main():
	if len(sys.argv)<2:
		csv_file = raw_input("Enter CSV File Path : ")
	else:
		csv_file = sys.argv[1]

	lr = LinearRegression(csv_file)
	print "Equation : ", lr.getEquation()
	while True:	
		x = float(raw_input("Enter value of x : "))
		print "Predicted Value of y : ",lr.predict(x)

if __name__ == '__main__':
	main()