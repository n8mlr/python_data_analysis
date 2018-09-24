import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_excel_file(filename, sheetname):
	"""Get a cleaned data frame

	Assumptions:
	* Report downloaded from Google Analytics named
		'Browser Window Sizes and Device Category'
	* GA Segment named 'Not a bot' was active, to avoid
		counting of AWS traffic

	:param filename:
	:return pandas.core.frame.DataFrame:
	"""
	unclean_frame = pd.read_excel(filename, sheetname)

	# Drop rows with NA values
	no_nas = unclean_frame.dropna()

	# Remove rows containing '(not set)'
	not_set = no_nas[no_nas['Browser Size'] == '(not set)']

	return no_nas.drop(not_set.index)

def flatten_frame(df):
	"""Returns a flattened dataframe

	:param df: pandas.core.frame.DataFrame
	:return pandas.core.frame.DataFrame:
	"""
	table = {
		"Browser Size": [],
		"Device Category": []
	}

	for row in df.values:
		num_occurences = int(row[2])
		for o in range(num_occurences):
			table["Browser Size"].append(row[0])
			table["Device Category"].append(row[1])

	# Initalize panda dataframe
	return pd.DataFrame(table)



def add_width_height_columns(df):
	"""Split width and height in to columns"""
	df["Width"] = df["Browser Size"].map(lambda val: int(val.split("x")[0]))
	df["Height"] = df["Browser Size"].map(lambda val: int(val.split("x")[1]))
	return df

def build_report_frame(excel_file_name, sheetname):
	"""Create a cleaned and transformed DataFrame ready for reporting"""
	cleaned = clean_excel_file(excel_file_name, sheetname)
	df = add_width_height_columns(flatten_frame(cleaned))
	return df

def graph_browser_sizes(df):
	plt.plot(df['Width'].values, df['Height'].values, 'ro', markersize=2)
	plt.xlabel("Width")
	plt.ylabel("Height")
	#plt.show()
	plt.savefig('outputs/sizes.png')