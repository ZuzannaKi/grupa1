# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("pre_proc.csv")

plt.scatter(dataset["X"],dataset["Y"],c=dataset["geoZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("geoportal1 - Z")
plt.colorbar(label="Difference")
plt.show()

plt.scatter(dataset["X"],dataset["Y"],c=dataset["upZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("up421 - Z")
plt.colorbar(label="Difference")
plt.show()