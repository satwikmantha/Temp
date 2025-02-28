import streamlit as st

# Title of the application
st.title("My Sample Streamlit Application")

# Sidebar with user input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age:", min_value=1, max_value=100, step=1)
color = st.sidebar.selectbox("Select your favorite color:", ["Red", "Blue", "Green", "Yellow"])

# Display output
st.write(f"Hello, **{name}**!")
st.write(f"You are **{age}** years old.")
st.write(f"Your favorite color is **{color}**.")

# Simple button interaction
if st.button("Click Me!"):
    st.success(f"Thank you, {name}! Have a great day! 🎉")

# Display an image
st.image("https://source.unsplash.com/random/400x200", caption="Random Image")

# Display a chart
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# Footer message
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

