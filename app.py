import streamlit as st;
import pandas as pd;
import numpy as np;

st.title("My streamlit app");
st.write("This is a simple text in streamlit app");
df=pd.DataFrame({
    "First col":[1,2,3,4],
    "Second col":[10,20,30,40]
})
st.write("This is a DataFrame");
st.write(df);

line_chart=pd.DataFrame(
    np.random.randn(20,3), columns=["A","B","C"]
)

st.line_chart(line_chart);