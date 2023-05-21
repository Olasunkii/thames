import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
import matplotlib.pyplot as plt
import os 

# Data handling dependencies
import numpy as np
import pandas as pd

from PIL import Image
from zipfile import ZipFile

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
# Load the weather data into a pandas DataFrame
data = pd.read_csv("data/thames_rainfall_data.csv") 


def streamlit_menu(example=1):
    # Display average values in a horizontal layout using Streamlit columns

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "About","Analysis","Downloads", "Contact"],  # required
            icons=["house", "people", "graph-down","download","telephone"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "12px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "4px",
                    "--hover-color": "#fafa",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=3)

if selected == "Home":
    # Calculate average values
    average_temp = data['temp_2m_celsius'].mean()
    average_humidity = data['specific_humidity_2m _gkg'].mean()
    average_wind_speed = data['wind_speed_10m_ms'].mean()
    average_pressure = data['surface_pressure_kPa'].mean()

    # Set up the Streamlit app layout
    st.title("Thames Climate Summary Dashboard")
    st.subheader("Current Climate Conditions")

    # Display average values in a horizontal layout using Streamlit columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Temperature (°C)", f"{average_temp:.2f}")

    with col2:
        st.metric("Specific Humidity (g/kg)", f"{average_humidity:.2f}")

    with col3:
        st.metric("Wind Speed (m/s)", f"{average_wind_speed:.2f}")

    with col4:
        st.metric("Surface Pressure (kPa)", f"{average_pressure:.2f}")

    # Sidebar controls for selecting time range and location
    st.sidebar.title("Filter Options")
    start_year = st.sidebar.slider("Select Start Year", min_value=2010, max_value=2017, value=int(data['year'].min()))
    end_year = st.sidebar.slider("Select End Year", min_value=2010, max_value=2017, value=2017)
    locations = sorted(data['location'].unique())
    selected_location = st.sidebar.selectbox("Select Location", locations)

    # Filter the data based on user selection
    filtered_data = data[(data['year'] >= start_year) & (data['year'] <= end_year) & (data['location'] == selected_location)]

    # Plot the rainfall patterns over time using a line chart
    fig = px.line(filtered_data, x='date', y='cdr_mm', title=f"Rainfall Patterns for {selected_location}")
    st.plotly_chart(fig)

    # Display the filtered data
    st.write(f"Rainfall Data for {selected_location} from {start_year} to {end_year}")
    st.write(filtered_data)
    
if selected == "About":
    st.title(f"You have selected {selected}")
if selected == "Analysis":
    st.title(f"You have selected {selected}")
if selected == "Downloads":
    st.title(f"You have selected {selected}")

        # Data Loading
    df_thames = pd.read_csv('data/thames_rainfall_data.csv')
    thm = list(df_thames['location'].unique())

    # App declaration
    def main():
        st.title('RAINFALL DATA API')

        #Thames Catchment Areas
        st.header('Thames River Basin')
        st.write('The Thames river basin district covers over 16,200 square kilometers. It encompasses all of Greater London and extends from north Oxfordshire southwards to Surrey and from Gloucester in the ' +
                    'west to the Thames Estuary and parts of Kent in the east. In total over 15 million people live in the Thames district with many entering daily to work or visit. In addition to ' +
                    'Greater London, other urban centres in the river basin district include Luton, Reading and Guildford. The Thames river basin district has a rich diversity of wildlife and habitats,' +
                    'supporting many species of global and national importance from chalk streams such as the River Kennet to the Thames Estuary and salt marshes. The management catchments that make up ' +
                    'the river basin district include many interconnected rivers, lakes, groundwater, estuarine and coastal waters. These catchments range from chalk streams and aquifers to tidal and ' +
                    'coastal marshes. The river basin district is mostly rural to the west and very urban to the east where it is dominated by Greater London. Around 17% of the river basin district is ' +
                    'urbanised and the rural land is mainly arable, grassland and woodland. The economy is dominated by Greater London and the finance sector.')
        st.write('This information was gotten from the UK Department for Environment, Food & Rural Affairs via https://environment.data.gov.uk/catchment-planning.')
        image1 = Image.open('images/thames2.jpeg')
        img1 = image1.resize((2000,1500))
        image2 = Image.open('images/thames1.png')
        img2 = image2.resize((2000,1500))
        image3 = Image.open('images/thames3.jpeg')
        img3 = image3.resize((2000,1500))
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(img1, caption=None, use_column_width=True)
        with col2:
            st.image(img2, caption=None, use_column_width=True)
        with col3:
            st.image(img3, caption=None, use_column_width=True)
        st.write('Operational Catchment Areas in the Thames River Basin.')
        thm_op = st.selectbox('Select Operational Catchment Area', thm)
        for i in range(len(thm)):
            if thm_op == thm[i]:
                df = df_thames[df_thames['location'] == thm[i]]
                csv = df.to_csv(index=False)
                st.download_button('Download', csv, thm[i]+'.csv', key = 'download-csv')
                if thm[i]+'.csv' in os.listdir():
                    os.remove(thm[i]+'.csv')

    if __name__ == '__main__':
        main()

if selected == "Contact":
    def contact_form():
        st.title("Contact Us")
        
        # Input fields for name, email, and phone number
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        
        # Text area for the message
        message = st.text_area("Message")
        
        # Submit button
        if st.button("Submit"):
            # Validate form inputs
            if not name:
                st.error("Please enter your name")
            elif not email:
                st.error("Please enter your email")
            elif not phone_number:
                st.error("Please enter your phone number")
            elif not message:
                st.error("Please enter a message")
            else:
                # Process the form submission
                # You can add your own logic here, such as sending an email or storing the form data in a database
                st.success("Thank you! Your message has been submitted.")
                st.info("We will get back to you soon.")
                # Clear form fields after submission
                name = ""
                email = ""
                phone_number = ""
                message = ""

    contact_form()

