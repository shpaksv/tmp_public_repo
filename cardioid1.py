import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


theta = np.arange(0, 4*np.pi, 0.01)
r = 2 * (1 - 3 * np.cos(theta))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
st.pyplot(fig)
