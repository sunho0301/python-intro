#If a question is asked of you, output the answer to the STDOUT (google-able
# term)
# There are multiple equally valid ways to accomplish many of these tasks

# import pandas and plotly. You may want to comment out the plotly import until
# you get to that part because the code runs much slower with it
import pandas
# from plotly.offline import plot
# import plotly.graph_objs as go

##################
# Python Warm-up #
##################

# Make a function which takes as arguments an array of names and a
# letter and returns an array of only the names which contained that
# letter. Print the result of calling your function on n_arr.
n_arr = ["Mike", "Linus", "Grace"]

def findNames(names, letter):
	new_list = []
	for name in names:
		if letter in name:
			new_list.append(name)
	return new_list


# BONUS: Do it without a loop


#####################
# Manipulating Data #
#####################

# Read the cost-data csv file into a pandas dataframe
ed_data = pandas.read_csv("data/cost-data.csv", encoding="iso-8859-1")

# Print the number of rows and columns in the data in the format
# rows=#, cols=#
shape = ed_data.shape
print("rows=%d, cols=%d" % shape)
print()

# Change the following column names in your data frame
# 2012-13 Tuition and fees  -> tuition.2012
# 2014-15 Tuition and fees  -> tuition.2014
# Sectior name              -> sector
# Name of institution       -> instituion
ed_data = ed_data.rename(columns={'2012-13 Tuition and fees': 'tuition.2012',
								'2014-15 Tuition and fees': 'tuition.2014',
								'Sector name': 'sector',
								'Name of institution': 'institution'})

# How many UNIQUE institutions are there? What data structure could you
# leverage?
inst = ed_data.get("institution")
#ed_data["institution"]
ninst = len(set(inst))
#set() <- only unique values

# What types of schools are there? How many of each type are there?
# Hint: You can do this using pandas or stock python


# Create a bar graph with sectors on the x axis and counts on the 
# y axis (using plotly)


#################################################################
# How did the cost of UW rank against other Washington schools? #
#################################################################

# Filter down to Washington schools, then compute the rank for 2014
wa_data = ed_data[ed_data.State == "WA"]
wa_data.is_copy = False
wa_data["tuition_rank"] = wa_data["tuition.2014"].rank(numeric_only=True)

rank = wa_data[wa_data.institution ==
               "University of Washington-Seattle Campus"].tuition_rank.iloc[0]
print("UW 2014 Tuition Rank: %d" % rank)	
print()

# Which *sector* had the largest average change in tuition?

#######################
# IF YOU FINISH EARLY #
#######################

# Come up with 3 questions you find interesting that can be answered by
# the data and figure out how to find the answers
