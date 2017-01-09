#If a question is asked of you, output the answer to the STDOUT (google-able
# term)
# There are multiple equally valid ways to accomplish many of these tasks

# import pandas and plotly. You may want to comment out the plotly import until
# you get to that part because the code runs much slower with it
import pandas
from plotly.offline import plot
import plotly.graph_objs as go

##################
# Python Warm-up #
##################

# Make a function which takes as arguments an array of names and a
# letter and returns an array of only the names which contained that
# letter. Print the result of calling your function on n_arr.
n_arr = ["Mike", "Linus", "Grace"]

def filter_names(names, letter):
    arr = []
    for n in names:
        if letter in n:
            arr.append(n)
    return arr

# BONUS: Do it without a loop
def names_bonus(names, letter):
    return list(filter(lambda n: letter in n, names))

print(filter_names(n_arr, "i"))
print(names_bonus(n_arr, "i"))
print()

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
                                  'Sector name': 'sector_name',
                                  'Name of institution': 'institution'})

# How many UNIQUE institutions are there? What data structure could you
# leverage?
inst = ed_data.get("institution")
ninst = len(set(inst))
print("Number of institutions: %d" % ninst)
print()

# What types of schools are there? How many of each type are there?
# Hint: You can do this using pandas or stock python

# Plain python method
sectors = {}
for index, row in ed_data.iterrows():
    s = row['sector_name']
    if s in sectors:
        sectors[s] += 1
    else:
        sectors[s] = 1

for k, v in sectors.items():
    print("%s: %d" % (k, v))
print()

# Pandas method
sector_counts = ed_data['sector_name'].value_counts();
print(sector_counts)
print()

# Create a bar graph with sectors on the x axis and counts on the 
# y axis (using plotly)
data = [go.Bar(
    x=sector_counts.axes[0].tolist(),
    y=list(sector_counts.values)
)]

plot(data)

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
change = ed_data.get("tuition.2014") - ed_data.get("tuition.2012")
ed_data['change'] = change
new_ed = ed_data\
            .groupby("sector_name")\
            .mean()

largest_sector = new_ed['change'].idxmax()
print("Sector with largest tuition change: %s" % largest_sector)
print()

#######################
# IF YOU FINISH EARLY #
#######################

# Come up with 3 questions you find interesting that can be answered by
# the data and figure out how to find the answers

# 1. What is the average tution in 2014 for schools in the PNW
pnw_data = ed_data[ed_data.State.isin(["WA", "OR", "ID"])]
avg = pnw_data.get("tuition.2014").mean()
print("Average pnw tuition: %.2f" % avg)
print()

# 2. Which school in sector 4 has the lowest tuition?
sec_4 = ed_data[ed_data.Sector == 4]
lowest = sec_4.institution[sec_4["tuition.2014"].idxmin()]
print("Lowest tuition in sector 4: %s" % lowest)
print()

# 3. Is python infinitely awesome?
print("Is python awesome? " + "yes" if 100000 < float('inf') else "no")
