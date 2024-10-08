# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
"""Read data"""
dataset = pd.read_csv(u"C:/Users/KN/Downloads/z_geoportal_up42.csv")

'''Calculate differences between Z and other height values'''
dataset=dataset.assign(geoZ = dataset["geoportal1"] - dataset["Z"])
dataset=dataset.assign(upZ = dataset["up421"] - dataset["Z"])

'''Plotting the results'''

plt.scatter(dataset["X"],dataset["Y"],c=dataset["geoZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("geoportal1 - Z")
plt.colorbar(label="Difference")
plt.show()

plt.scatter(dataset["X"],dataset["Y"],c=dataset["upZ"],s=0.01,marker="s",cmap = "seismic")
plt.title("up421 - Z")
plt.colorbar(label="Difference")
plt.show()