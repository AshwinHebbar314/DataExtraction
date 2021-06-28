# %%
import pandas as pd
import json
import xlrd

df = pd.read_json("sampleparentdirectory.json")
df = df.transpose()

clubname02 = xlrd.open_workbook("clubdatarandom.xlsx")
sheetnames = clubname02.sheet_names()

jsondictinner = {}
df["Email Address"] = df.index
for sheet in sheetnames:
    clubname = pd.read_excel("clubdatarandom.xlsx", sheet_name=sheet)
    clubname["Email Address"] = clubname["Email Address"].apply(
        lambda x: x.split("@")[0])
    clubnamefinal = pd.merge(clubname, df, on="Email Address", how="inner")
    clubnamefinal = clubnamefinal.set_index("Email Address")
    clubnamefinal = clubnamefinal.transpose()
    clubnamefinal.to_json("output_club_list.json")
    with open('output_club_list.json') as json_file:
        jsondict = json.load(json_file)
    jsondictinner[sheet] = jsondict


with open("output.json", "w") as outfile:
    json.dump(jsondictinner, outfile)
# %%
