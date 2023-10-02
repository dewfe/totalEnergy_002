import pandas as pd

fd = pd.read_csv("data\\bristell_001.csv", delimiter=";")
print(fd.head())
print(fd.dtypes)
fd["iasMps"] = fd["ias"] * 1.852 / 3.6
fd["tasMps"] = fd["tas"] * 1.852 / 3.6
fd["gsMps"] = fd["gs"] * 1.852 / 3.6
fd["vvMps"] = fd["vv"] * 0.00508
print(fd.dtypes)
print(fd[["vv", "vvMps"]])