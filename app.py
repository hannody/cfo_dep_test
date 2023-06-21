"""
# My first app
Here's our first attempt at using data to create a table:
"""
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('Welcome')

st.set_option('deprecation.showPyplotGlobalUse', False)

# Create DataFrame
df = pd.DataFrame({
    'lat': [3.1319, 3.2, 3.1, 4],
    'lon': [101.6841, 102, 101.0, 101.40]
})

df

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.bar_chart(df)

st.color_picker('Pick A Color', '#00f900')

st.area_chart(df)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

option = st.selectbox(
    'Which number do you like best?',
     df['lat'])

'You selected: ', option


import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 100, (25, 75)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")




# Create DataFrame
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y1': [10, 20, 30, 40],
    'y2': [20, 30, 40, 50]
})

# Plot area chart using pandas and Matplotlib
df.set_index('x', inplace=True)
plt.fill_between(df.index, df['y1'], df['y2'], alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Area Chart')
st.pyplot()


# Create DataFrame
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'values': [30, 40, 20, 10]
})

# Plot pie chart using pandas and Matplotlib
plt.pie(df['values'], labels=df['category'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Pie Chart')
st.pyplot()
