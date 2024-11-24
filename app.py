# Installation

# To install streamlit, you can either work on your local system or in a virtual environment.

# pip install streamlit

# Or if you want to use it in a virual environment like pipenv.

# pipenv install streamlit

# After installation you can then use the CLI to run your app and display it in your default browser on localhost port(eg localhost:8501)

# To run your app, you can use

# streamlit run app.py

# or with pipenv

# pipenv run streamlit run app.py

# streamlit --help


import streamlit as st

# Working with Text

# Text/Title
st.title("My First Streamlit App")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello my first streamlit app")

# Markdown

st.markdown("### This is a Markdown")


## Working with Colorful Text and Error Messages

st.success("sucessful")

st.info("Information")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError ('name three not defined')")

# Getting Help Info About Python

# Get Help
st.help(range)

# Writing Text Super Function

# Using the Write Function For More

# The st.write() allows us to do more ,not just out put text 
# but also python functions,object,etc

st.write("Hello, World!")
st.write("Hello, World!", "danger")
st.write(range(20))


## IMAGES
from PIL import Image
img = Image.open("images.jpeg")
st.image(img, caption="My Image", width=300)

# VIDEOS
vid_file = open("sample.mp4", "rb").read()
# rb:-> read byte
# vid_bytes = vid_file.read()
st.video(vid_file)

# AUDIO
audio_file = open("sample.mp3", "rb")
st.audio(audio_file, format="audio/mp3")


## Widget: Checkbox,Selectbox,Radio button,etc

# Checkbox
if st.checkbox("Shoe/Hide"):
    st.text("Showing or Hiding Widget")
    
# Radio Button
status = st.radio("what is your status",("Active", "Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.error("You are Inactive")
    
# SelectBox

occupation = st.selectbox("Your Occupation",["Programmer", 
                                             "DataScientist",
                                             "Doctor",
                                             "Bussinessman",
                                             "Teacher"])

st.write("You selected:", occupation)

# MultiSelect
location =  st.multiselect("Your Location:[Where do you work]",("New York",
                                                                "Los Angeles", 
                                                                "Chicago", 
                                                                "Houston"))
st.write("You selected:", len(location), "locations")

st.write("Locations:", location)

# Slider
level = st.slider("How much do you like this product?", 1, 10)

# Buttons
st.button("Simple Button")
if st.button("Danger Button"):
    st.error("You clicked the danger button")
    

# How to receive user input and process them with streamlit?

# This is the most input aspect for the end user. 
# How do you receive the users input and do something with it. 
# You can use the st.text_input() to enable you achieve such 
# a functionality.

## Receiving User Text Input
firstname = st.text_input("Enter Your Firstname", "Type Here....")
if st.button("submit"):
    result = firstname.title()
    st.success(result)

# TEXT
message = st.text_area("Enter Your message", "Type Here...")
if st.button("Submit"):
    result = message.title()
    st.success(result)
    
# Date Input
import  datetime
today = st.date_input("Today is", datetime.datetime.now())
st.write("Today is", today)

# Time
the_time = st.time_input("The time is", datetime.time())


# Displaying Raw Code and JSON

# In case you want to display the raw preformatted code 
# you can use the st.code() or st.echo()

# Displaying Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code 

with st.echo():
# This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

#  Displaying JSON

# Displaying JSON
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})

# Displaying Progressbars,Spinners and Balloons

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
# other plotting actions...
st.pyplot(fig)

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")


# Balloons
st.balloons()

# Working with Data Science (DataFrame,Plot,Tables,etc)

# Streamlit has features for working directly with dataframes and 
# plot. You can create nice plot with the st.pyplot() ,st.line_chart(),
# st.altair_chart() and more visualizations.

# Documentation :-> [https://docs.streamlit.io/]

# Plot
st.pyplot()

# DataFrames
st.dataframe(df)

# Tables
st.table(df)


# Showing Sidebars

# With streamlit you can create sidebars with ease. 
# For now you can use any of the functions except st.write,
# st.echo,st.code with the sidebar method.

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

# Working with Functions

# You can also work with functions and classes in streamlit like 
# how you do any python work. To improve the speed and performance 
# of your functions you can use the @st.cache to hide and cache data.

# Normal Function
def run_fxn():
    return range(100)

st.write(run_fxn())

# To Improve Performance/Speed via caching
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

