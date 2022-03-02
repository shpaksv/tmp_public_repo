import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


theta = np.arange(0, 2*np.pi, 0.01)
r = 2 * np.cos(2.5*theta) * np.cos(5*theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
st.pyplot(fig)
