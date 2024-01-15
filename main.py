import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for the Next Days")
place=st.text_input("Place:")
days=st.slider("Forcast Days",min_value=1,max_value=5,help="Select the number of forecast days")
option=st.selectbox('Select Data to view',('Temperature','Sky'))
st.subheader(f"{option} for the next {days} days in {place}")
temperature=[]
if place:
    try:
        filtered_data=get_data(place,days,option)
        if option=="Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            for temp in temperatures:
                temperature.append(float(temp)-273)
            figure=px.line(x=dates,y=temperature,labels={"x":"Date","y":"Temperature(C)"})
            st.plotly_chart(figure)
        if option =="Sky":
            images={"Clear": "images/clear.png","Clouds": "images/cloud.png","Rain": "images/rain.png","Snow": "images/snow.png"}
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths=[images[condition] for condition in filtered_data]
            st.image(image_paths,width=115)
    except KeyError:
        st.write("This place does not exist")
