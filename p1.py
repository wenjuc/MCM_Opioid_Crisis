import sys
import pandas as pd
from geopy import geocoders  
gn = geocoders.GeoNames(username='doomibox')

print "reading data"
df = pd.read_csv("2018_MCMProblemC_DATA/updated_nflis_data.csv")
df = df.assign(Location = lambda x: x.County + ", " + x.State)

f = open("out/out.csv", "w")
def write_csv(file, lst):
	for i, item in enumerate(lst):
		if i != 0:
			file.write(",")
		if type(item) != str:
			file.write(str(item))
		else:
			file.write("\"" + item + "\"")
	file.write("\n")

loc_list = set(df['Location'])

write_csv(f, ['Year', 'Location', 'Substance', 'DrugReports', 'County_Rate', 'change'])
for i, substance in enumerate(set(df['SubstanceName'])):
	print i, substance
	for location in loc_list:
		info = df.loc[(df['SubstanceName'] == substance) & (df['Location'] == location)]
		for year in range(2011, 2018):
			curr_year = info[info['Year']== year]
			last_year = info[info['Year']== year - 1]
			c_val = 0.1 if len(curr_year) == 0 else curr_year['County_Rate'].item()
			l_val = 0.1 if len(last_year) == 0 else last_year['County_Rate'].item()
			dr = 0 if len(curr_year) == 0 else curr_year['DrugReports'].item()
			cr = 0 if len(curr_year) == 0 else curr_year['County_Rate'].item()
			change = (c_val - l_val) / float(l_val)
			write_csv(f, [year, location, substance, dr, cr, change

f.close()			


# print "writing to out/out.csv"
# new_df.to_csv("out/out.csv")