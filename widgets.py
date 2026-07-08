import streamlit as st;
import pandas as pd;

st.title("Streamlit text input");
name=st.text_input("Enter your name: ");

age=st.slider("Select your age: ",1,100,25);
st.write(f"Your age is: {age}");
if name:
    st.write(f"Hello, {name}!");

options=["Python", "Java", "Cpp", "JS"];
choice=st.selectbox("Select your Programming language: ", options);
st.write("Selected Language is: ",choice);

data={
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
};
df=pd.DataFrame(data);
df.to_csv("sample_data.csv", index=False);
st.write(df);

upload_file=st.file_uploader("Choose a CSV file", type="csv");
if upload_file is not None:
    df=pd.read_csv(upload_file);
    st.write(df);