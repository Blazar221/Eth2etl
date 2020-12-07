import csv
from config import CSV_PATH


def save_csv(filename, data):
	with open(CSV_PATH + filename + '.csv', 'a') as f:
		writer = csv.writer(f)
		for line in data:
			writer.writerow(line)
