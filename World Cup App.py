#------------------ pip installs
#pip install streamlit
#pip install protobuf // #pip install --upgrade protobuf

#------------------ run streamlit
# streamlit run "C:\Users\c17527k\Documents\My Experiments\Python Scripts\World Cup App.py"

#------------------ load packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# title and intro text
st.title('World Cup :soccer: :trophy: Explore Page :page_facing_up:')
st.text('This web app will enable you to explore some historical World Cup data.')

# view count
st.subheader('Traffic :traffic_light: on this page')
col1, col2, col3 = st.columns(3)
col1.metric("Local temperature", "67 °F", "10.2 °F")
col2.metric("Developer", "1", "0%", delta_color="off")
col3.metric("Page visit", "86%", "-4%")

# create a file uploader object
upload_file = st.file_uploader('Please upload a file containing world cup data.')

if upload_file is not None:
    # read the file to  df using pandas
    df = pd.read_csv(upload_file)
    
    # table
    st.subheader('A sneak peak :eyes: of the :blue[table]')
    st.table(df.head(2))
    
    # time : attendance
    st.subheader(':blue[Visualizations] :bar_chart:')
    fig, ax = plt.subplots(1,1)
    ax.set_title('Has sports viewing (in person) become more popular overtime?')
    ax.scatter(x=df['Year'], y=df['Attendance'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Attendance')
    st.pyplot(fig)
    
    # games : goals
    fig, ax = plt.subplots(1,1)
    ax.set_title('Do you score more the more you play?')
    ax.scatter(x=df['MatchesPlayed'], y=df['GoalsScored'])
    ax.set_xlabel('MatchesPlayed')
    ax.set_ylabel('GoalsScored')
    st.pyplot(fig)
    
    # country : score
    fig = px.bar(df,x='GoalsScored',y='Country', orientation='h', color='Year', title='How many shots have been taken by each country?')
    st.write(fig)
    
    # survey
    option = st.selectbox(
        'Did you enjoy this sandbox?',
        ('Yes', 'No')
        )

    st.write('You selected:', option)
    st.write('Thanks for your input.')
    
    