import sys
import pandas as pd

filepath = sys.argv[1]

print "reading from " + filepath

print "reading drug_report"
drug_report = pd.read_excel(filepath, sheet_name="FIPS", converters={"FIPS_Combined":int})

print "reading geo_info"
geo_info = pd.read_excel(filepath, sheet_name="GEO")

print "merging"
df = drug_report.merge(geo_info, left_on="FIPS_Combined", right_on="GEO.id2")

filename, file_ext = filepath.split(".")
newpath = filename + "_merged." + file_ext
print "writing to " + newpath
df.to_excel(newpath, sheet_name="merged")



