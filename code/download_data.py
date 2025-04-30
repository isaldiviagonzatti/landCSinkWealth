import os
import urllib.request

rawDir = "../data/raw/"
filename = "raw_scc_SSP2_rcp60_constant_bootstrap_climensemble_hmqrs.csv"
url = "https://www.dropbox.com/scl/fi/qlxnntf3kelfeocmt0te2/raw_scc_SSP2_rcp60_constant_bootstrap_climensemble_hmqrs.csv?rlkey=53y8xoysiksq35xlzocrlepvr&st=h4ss2dd7&dl=1"

os.makedirs(rawDir, exist_ok=True)
filepath = os.path.join(rawDir, filename)

if not os.path.exists(filepath):
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filepath)
    print("Download complete.")
else:
    print(f"{filename} already exists.")
