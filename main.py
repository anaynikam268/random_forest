import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a simple streamlit app")
st.radio("Choose Option:",["Option 1","Option 2","Option 3"])
st.button("Click me")
st.text_input("Enter some text:")
st.slider("Select a value: ",0,100,50)
st.checkbox("Check me out")
st.selectbox("Pick one: ",["Choice 1","Choice 2","Choice 3"])
