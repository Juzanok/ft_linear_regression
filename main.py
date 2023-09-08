import csv
import sys

try :
	with open("./theta.csv", 'r') as file:
		csvreader = csv.reader(file, delimiter=',')
		row = next(csvreader)
		if len(row) != 2 :
			raise ValueError("wrong number of arguments in theta.csv")
		theta0 = float(row[0])
		theta1 = float(row[1])
except FileNotFoundError :
	theta0 = 0
	theta1 = 0
except ValueError as error :
	sys.exit(f"Error: {error}")
except Exception:
	sys.exit("Error: bad theta.csv file")

check = False
while check == False :
	mileage = input("Enter mileage: ")
	try :
		mileage_num = float(mileage)
		if (mileage_num > 0) :
			check = True
		else :
			print("Error: mileage can not be negative, try again.")
	except :
		print ("Error: not a number, try again.")

prediction = theta0 + theta1 * mileage_num
print (f"Predicted price for {mileage_num} miles: {prediction}")
