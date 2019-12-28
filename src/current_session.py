# coding: utf-8
data = pd.read_csv("2019-12-27_21-59-04_36C3.csv")
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("2019-12-27_21-59-04_36C3.csv")
data.set_index("Time (s)")
data.index = ["time", "ax", "ay", "az", "abs"]
data
data.columns = ["time", "ax", "ay", "az", "abs"]
data.ax.plot(label="ax")
data.ay.plot(label="ay")
data.az.plot(label="az")
plt.show()
data.ax.plot(label="ax")
data.ay.plot(label="ay")
data.az.plot(label="az")
plt.legend()
plt.show()
data
data.set_index("time")
data
data.set_index("time", inplace=True)
data
data.ax.plot(label="ax")
data.ay.plot(label="ay")
data.az.plot(label="az")
plt.legend()
plt.show()
import numpy as np
get_ipython().run_line_magic('pinfo', 'data.insert')
data.insert(loc=len(data.columns), column="ax_m", value=data.ax - data.ax.mean())
data
data.insert(loc=len(data.columns), column="ay_m", value=data.ay - data.ay.mean())
data.insert(loc=len(data.columns), column="az_m", value=data.az - data.az.mean())
data
data.az_m.plot()
plt.show()
data.az_m.plot()
1/0.005
data.az_m.resample("10ms").mean().plot()
data.index = pd.to_datetime(data.index)
data
get_ipython().run_line_magic('save', 'dataProcessing')
get_ipython().run_line_magic('save', 'current_session')
get_ipython().run_line_magic('save', 'current_session ~0/')
