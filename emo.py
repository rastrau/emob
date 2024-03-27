# Python 3.9
import os
import zipfile
import requests
import datetime

urls = ["https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/oicp/ch.bfe.ladestellen-elektromobilitaet.json",
        "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/status/oicp/ch.bfe.ladestellen-elektromobilitaet.json",
        "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/ch.bfe.ladestellen-elektromobilitaet_de.json"
        ]

filenames = []
for url in urls:
    print("Download %s..." % url)
    request = requests.get(url)

    filename = url.split("/")[-1]
    if "status" in url:
        filename = filename.replace(".json", "-status.json")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(request.text)
        filenames.append(filename)
        print("\tDone.")

now = datetime.datetime.now()
sharding_path = now.astimezone(datetime.timezone.utc).strftime("%Y-Week-%V")

if not os.path.exists(sharding_path):
    os.makedirs(sharding_path)

zipfilename = now.astimezone(
    datetime.timezone.utc).strftime("%Y-%m-%dT%H%M%S.zip")
with zipfile.ZipFile(os.path.join(sharding_path, zipfilename),
                     "w", compression=zipfile.ZIP_LZMA) as zf:
    for filename in filenames:
        zf.write(filename)
        os.remove(filename)

