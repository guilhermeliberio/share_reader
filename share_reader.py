import os
import csv
import pprint as pp

share_dict = {}
files = [os.path.join('Shares\\FIN_CORP_RESTR\\', 'FIN_CORP_RESTR_CURATED.txt'), os.path.join('Shares\\FIN_CORP_RESTR\\', 'FIN_CORP_RESTR_RAW.txt'),
         os.path.join('Shares\\FIN_FL_RESTR\\', 'FIN_FL_RESTR_CURATED.txt'), os.path.join('Shares\\FIN_FL_RESTR\\', 'FIN_FL_RESTR_RAW.txt'),
         os.path.join('Shares\\FIN_GENERAL\\', 'FIN_GENERAL_CURATED.txt'), os.path.join('Shares\\FIN_GENERAL\\', 'FIN_GENERAL_RAW.txt'),
         os.path.join('Shares\\FIN_UPST_RESTR\\', 'FIN_UPST_RESTR_CURATED.txt'), os.path.join('Shares\\FIN_UPST_RESTR\\', 'FIN_UPST_RESTR_RAW.txt')]

for file in files:
    f = open(file, 'r')
    count = 1
    for line in f.readlines():
        if "share" in line and "--" not in line and line[0] != "!":
            splits = line.split(" to share ")
            key = splits[-1].strip()[0:-1]
            value = splits[0].strip().split(" ")[-1].strip('""')
            if "VWS" in value:
                if "_EU_" in value: value = value.replace("_EU_", "")
                elif "_AP_" in value: value = value.replace("_AP_", "")
                elif "_AM_" in value: value = value.replace("_AM_", "")
                else:
                    last_split = value.split("_")[-1]
                    if last_split in "EUAPAMG3S8XTID":
                        value = value.replace("_" + last_split, "")
                if key not in share_dict: share_dict[key] = [value]
                elif value not in share_dict[key]: share_dict[key].append(value)
        
with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in share_dict.items():
        writer.writerow([key, value, len(value)])

    