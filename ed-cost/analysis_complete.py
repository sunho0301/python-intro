# If a question is asked of you, output the answer to the STDOUT (google-able
# term)
# There are multiple equally valid ways to accomplish many of these tasks

# import pandas and plotly
import pandas

##################
# Python Warm-up #
##################

# Make a function which takes as an argument an array of names and a
# letter and returns an array of the names which contained those
# letters.
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
ed_data = pandas.read_csv("data/cost-data.csv", encoding="ISO-8859-1")

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
ninst = len(set(inst))
print("Number of institutions: %d" % ninst)
print()

# What types of schools are there? How many of each type are there?
sectors = set(ed_data.get('sector'))
print(' / '.join(sectors))
print()

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
            .groupby("sector")\
            .mean()

largest_sector = new_ed['change'].idxmax()
print(largest_sector)
print()
