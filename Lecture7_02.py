import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

row= np.random.randn(1,1)
'Growing line chart'
chart=st.line_chart(row)

for i in range(1,100):
    new_rows= row[0]+ np.random.randn(1,1)
    chart.add_rows(new_rows)
    row= new_rows
    time.sleep(0.05)

    values= np.random.rand(10)
    'matplotlibs line chart:'
    fig, ax = plt.subplots()
    ax.plot(values)
    st.pyplot(fig)
