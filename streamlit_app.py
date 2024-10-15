import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎈 My new app")

st.write(
"Analysis of travel times home to school"
)

st.title('Upload your CSV file')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write(df.head(10))

    # Select columns for scatter plot
    columns = df.columns.tolist()
    x_axis = st.selectbox('Select X-axis column', columns)
    y_axis = st.selectbox('Select Y-axis column', columns)
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[x_axis], df[y_axis])
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f'Scatter Plot of {x_axis} vs {y_axis}')
    
    # Display scatter plot
    st.pyplot(fig)