import pandas as pd
import numpy as np
import random as rnd
import pickle as pkle
import os.path
import streamlit as st
import plotly.express as px
import plotly.colors as pcolors
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Simulating a game of coin tosses with Monte Carlo", page_icon='🔢',layout="wide")

def local_css(file_name):
   with open(file_name) as f:
         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')

if "intro" not in st.session_state:
    st.session_state["intro"] = False

st.session_state.intro = True

if "ran" not in st.session_state:
    st.session_state["ran"] = rnd.randint(1,10000)

author_pic = Image.open('sganguly pp sized.jpeg')

with st.sidebar:
   st.image(author_pic)
   col1,col2,col3 = st.columns([1,10,1])
   with col2:
    st.markdown('Created by Shubharup Ganguly')

def gen_number():
    st.session_state["ran"] = rnd.randint(1, 10000)
    return

data_file = open("pkld_data_final.pkl")

if data_file:
    converge = pd.read_pickle('pkld_data_final.pkl')
else:
    converge = pd.DataFrame([[iterations, estimated, error]], columns=['N_points','estimate',"error"])

if st.session_state['intro']:

    with st.sidebar:

        st.markdown("# Simulation Parameter")
        st.markdown("Enter the number of trials. (Each trial has three tosses)")
        iterations = st.number_input("Total Number of trials:", min_value=1, max_value = 10000, value=st.session_state["ran"])
        st.button("Random number", on_click=gen_number)

    from coin_toss_functions import monte_carlo_estimate

    estimated = monte_carlo_estimate(iterations)
    actual = 0.5

    # #calculate the percent difference from the standard: |value - true_value|/|true_value|*100%
    diff_percent = (abs(estimated - actual)/actual)*100

    with st.sidebar:
        st.write("Number of trials:",iterations)
        st.write("Your estimate $\\hat{p}$ = ", estimated)
        st.write("True Value of $p$:", actual)
        st.write("The percent error between your estimation and the true value is:", round(diff_percent,3), "%")

converge = pd.concat([converge, pd.DataFrame([iterations, estimated, diff_percent], columns=converge.columns)], ignore_index=True)

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

colA, colB, colC = st.columns([1,2,1])
with colB:
    st.title('''Monte Carlo simulation''')
    st.markdown('''### for an interesting coin toss problem''')

st.header("Problem Statement")

problem_statement = read_markdown_file("problem_statement.md")

st.markdown(problem_statement)


st.header("Solution using Probability Theory")

theoretical_solution = read_markdown_file('theoretical_solution.md')

math = st.expander("Display Math")
with math:
    st.markdown(theoretical_solution)

st.write("---")

st.header("Motivation for Monte Carlo simulation")

monte_carlo_motiv = read_markdown_file('monte_carlo_motivation.md')

st.markdown(monte_carlo_motiv)

st.write("---")

st.header('How it works')
    
col1,col2 = st.columns(2)
with col1:

    st.write("""
From the sidebar type a number in the field (or use the plus/minus button) for \
the total number of trials you want to use to estimate $\\hat{p}$.""")

st.write("---")
   
st.header("How the total number of trials affects $\\hat{p}$")

st.write("""
            Following from the Law of Large Numbers, 
            with increasing number of trials, 
            the estimated $\hat{p}$ 
            should converge to the theoretically calculated probability $p$.""")

color = st.radio("Color points by:", ["Number of trials", str("% Error")])
range = st.slider("Range of calculated probability values:",0.0,1.0,[0.0,1.0],0.01)
range = [range[0]-0.05, range[1]+0.05]

if color == "Number of trials":
        column = "N_points"
else:
    column = "error"

error = (abs(estimated - actual)/actual)*100

# check if a pickled file with all the previous dat is there, if not create Data
# this will check for or create a new pkl file in main directory on streamlit servers

#plot the convergence

if column == 'N_points':
    fig2 = px.scatter(
            x=converge['N_points'],
            y=converge['estimate'],
            color=converge[column],
            color_continuous_scale = px.colors.sequential.Sunsetdark,
            labels={'x':"Number of trials",'y':"Calculated probability", 'color':"Number of trials"})
            #size=1)
    
elif column == "error":
    converge2 = converge.loc[converge['estimate'] > float(range[0]), :]
    converge2 = converge2.loc[converge['estimate'] < float(range[1]), :]

    fig2 = px.scatter(
            x=converge2['N_points'],
            y=converge2['estimate'],
            color=converge2['error'],
            color_continuous_scale = px.colors.sequential.Sunsetdark,
            labels={'x':"Number of trials",'y':"Calculated probability", 'color':"% Error"})
            #size=1)

fig2.update_layout(yaxis=dict(range=range))
fig2.add_shape(
    type="line",
    x0=0, x1=len(converge),
    y0=actual, y1=actual,
    line_color="red")

#send figure to streamlit
st.plotly_chart(fig2)

st.write("---")
# add in graph on how the % errors change as iterations are increased!

st.header('% Error as Iterations Change')

st.write("""
A great way to visually show how extreme the change in error is as we increase \
the number of points used in your simulation, is to plot each % Error as a function of \
the number of points!

As we would hope to see, the error percentage steadily declines with increasing number of trials.
         
To better see the spread in the points you can log the axes of both the y-axis \
(the % error) and the x-axis (the number of points).""")

    # add checkboxes to sidebar to make the axes log!
st.markdown("""
##### % Error Graph Parameters
To see the details of the error graph you can log one or both axes \
of the graph. This will display the order of magnitude of the percent error and total number of points.""")

x_log = st.checkbox("log Number of trials")
y_log = st.checkbox("log % Error")

fig2 = px.scatter(
        x=converge['N_points'],
        y=converge['error'],
        color=converge['N_points'],
        color_continuous_scale = px.colors.sequential.Sunsetdark,
        log_y=y_log, log_x=x_log,
        labels={'x':"Number of trials used in estimation",'y':"% Error",'color':"# of Points"})
        #size=1)
st.plotly_chart(fig2)

#repickle file with added data
converge.to_pickle('pkld_data_final.pkl')
