import sys
import pandas as pd
import numpy as np

print "reading drug_report"
nflis = pd.read_excel('MCM_NFLIS_Data.xlsx', sheet_name='Data')



for i in range(10, 17):
	filename = "ACS_" + str(i) + "_5YR_DP02"
	print "reading geo_info " + filename
	year = int("20" + str(i))
	filepath = filename + '/' + filename + "_with_ann.csv"
	geo_info = pd.read_csv(filepath)
	curr_year = nflis[nflis['YYYY']==year]

	curr_year = curr_year.groupby(['YYYY', 'FIPS_Combined', 'COUNTY', 'State'], as_index=False, group_keys=False).agg({'TotalDrugReportsCounty': np.sum})

	print "merging"
	print list(curr_year.columns)
	df = curr_year.merge(geo_info, left_on="FIPS_Combined", right_on="GEO.id2")

	newpath = "out/" + str(year) + "_merged.csv"
	print "writing to " + newpath
	df.to_csv(newpath)



# print "reading geo_info"
# geo_info = pd.read_excel(filepath, sheet_name="GEO")

# print "merging"
# df = nflis.merge(geo_info, left_on="FIPS_Combined", right_on="GEO.id2")

# filename, file_ext = filepath.split(".")
# newpath = filename + "_merged." + file_ext
# print "writing to " + newpath
# df.to_excel(newpath, sheet_name="merged")



