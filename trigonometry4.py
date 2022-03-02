import streamlit as st
import matplotlib.pylab as plt
import numpy as np

fig, ax = plt.subplots()
x1 = np.arange(0.00, 10*np.pi, 0.01)
y1 = np.power(np.cos(x1), 2) + np.power(np.sin(x1), 2)
y2 = np.sin(x1) - np.cos(x1)
y3 = np.sin(x1) + np.cos(x1)
ax.plot(x1, y1, 'b-', x1, y2, 'r-', x1, y3, 'k-',)

st.pyplot(fig)
