# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Read data"""

dataset = pd.read_csv(u"C:/Users/KN/Downloads/z_geoportal_up42.csv")
df = dataset.copy()
df = df.apply(np.round,args=(2,))
df = df.astype("float32")
df.to_pickle("pre_proc_bin")

'''Read pickled data'''

data = pd.read_pickle("pre_proc_bin")

'''Calculate differences between Z and other height values'''
data=data.assign(geoZ = data["geoportal1"] - data["Z"])
data=data.assign(upZ = data["up421"] - data["Z"])

'''Plotting the results'''

plt.scatter(data["X"],data["Y"],c=data["geoZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("geoportal1 - Z")
plt.colorbar(label="Difference")
plt.show()

plt.scatter(data["X"],data["Y"],c=data["upZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("up421 - Z")
plt.colorbar(label="Difference")
plt.show()

plt.hist(data["geoZ"],bins=100)
plt.show()
plt.hist(data["upZ"],bins=100)
plt.show()

mae_geoZ = sum(abs(data["geoZ"].fillna(0)))/data.shape[0]
print(f"MAE (geoportal): {mae_geoZ}")
mae_upZ = sum(abs(data["upZ"].fillna(0)))/data.shape[0]
print(f"MAE (up421): {mae_upZ}")