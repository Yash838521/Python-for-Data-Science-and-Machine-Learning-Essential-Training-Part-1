import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names=['column1','column2', 'column3']
data= pd.DataFrame(np.random.randint(30, size=(30,3)), columns=col_names)
#Creates a Pandas DataFrame with 30 rows and 3 columns filled with random numbers between 0 and 29, and assigns column names from col_names.

'line graph:'
st.line_chart(data)

'bar graph:'
st.bar_chart(data)

animals=['cat', 'cow','dog']
heights=[30,150,80]

'pie chart'
fig,ax = plt.subplots()
ax.pie(heights, labels=animals)
st.pyplot(fig)
