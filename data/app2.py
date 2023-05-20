import streamlit as st
import pandas as pd
import folium
import matplotlib.pyplot as plt

# Load the weather data into a pandas DataFrame
data = pd.read_csv("data/thames_rainfall_data.csv")  # Replace "your_weather_data.csv" with your actual file name

# Calculate average values
average_temp = data['temp_2m_celsius'].mean()
average_humidity = data['specific_humidity_2m _gkg'].mean()
average_wind_speed = data['wind_speed_10m_ms'].mean()
average_pressure = data['surface_pressure_kPa'].mean()

# Set up the Streamlit app layout
st.title("Weather Summary Dashboard")
st.subheader("Current Weather Conditions")

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





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the weather data into a Pandas DataFrame
data = pd.read_csv("data/thames_rainfall_data.csv")

# Sidebar - Location selection
selected_location = st.sidebar.selectbox("Select Location", data["location"].unique())

# Filter data based on selected location
filtered_data = data[data["location"] == selected_location]

# Line chart - Temperature over time
st.subheader("Temperature Trend")
plt.figure(figsize=(10, 6))
plt.plot(filtered_data["date"], filtered_data["temp_2m_celsius"], marker="o")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
st.pyplot(plt)

# Line chart - Wind speed over time
st.subheader("Wind Speed Trend")
plt.figure(figsize=(10, 6))
plt.plot(filtered_data["date"], filtered_data["wind_speed_10m_ms"], marker="o")
plt.xlabel("Date")
plt.ylabel("Wind Speed (m/s)")
plt.xticks(rotation=45)
st.pyplot(plt)

# Line chart - Humidity over time
st.subheader("Humidity Trend")
plt.figure(figsize=(10, 6))
plt.plot(filtered_data["date"], filtered_data["relative_humidity_2m_percentage"], marker="o")
plt.xlabel("Date")
plt.ylabel("Relative Humidity (%)")
plt.xticks(rotation=45)
st.pyplot(plt)
