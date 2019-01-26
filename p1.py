import pandas as pd
from geopy import geocoders  
gn = geocoders.GeoNames(username='doomibox')

print "reading excel"
df = pd.ExcelFile("2018_MCMProblemC_DATA/MCM_NFLIS_Data.xlsx").parse(1)
print list(df.columns.values)

print "creating location variables"
df = df.assign(location = lambda x: x.COUNTY + ", " + x.State)

print df.iloc[0].location, gn.geocode(df.iloc[0].location)



print "writing to out/out.xlsx"
df.to_excel("out/out.xlsx")