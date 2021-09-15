import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import time

def app():
    
    file = st.file_uploader("Upload file")
    show_file = st.empty()
    
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join([".csv", ".xls", ".xlsx"]))
        return
    
    label = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        # Update progress bar with iterations
        label.text(f'Loaded {i+1} %')
        bar.progress(i+1)
        time.sleep(0.01)
    
    path = file
    data = pd.read_csv(path)
    data = data.fillna(data.mean(axis = 0))
    st.write(data)
    
    st.write("")
    st.write("")
    
    data = data.melt(id_vars=["Country Name", "Country Code"], var_name = "Year", value_name = "Interest Rate")
    data.sort_values(["Country Name", "Year"], inplace = True)
    data = data.reset_index()
        
    if st.checkbox("Interest Rate through the World"):
        fig = go.Figure()
        fig = px.bar(data, x="Year", y="Interest Rate", text = "Interest Rate", animation_frame = "Country Name", color='Country Name', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Interest Rate (%)", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=600, width=1600, title_text="Interest Rates from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
       
    if st.checkbox("Interest Rate of Nigeria"):
        df = data[data["Country Name"] == "Nigeria"]
        
        fig = go.Figure()
        #fig = px.line(df, x="Year", y="Interest Rate", color="Year", text="Interest Rate")
        fig = go.Figure(data=go.Scatter(x=data.Year, y=df["Interest Rate"], mode='lines+markers'))
        fig.update_xaxes(title_text = "Year", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Interest Rate (%)", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(0,202,225)', marker_line_width=1.5)
        fig.update_layout(height=600, width=1600, title_text="Interest Rate of Nigeria from 1960-2020") 
        #fig.add_annotation(x=1993, y=31.95, text="Highest Recorded Interest Rate for Nigeria in 1993", showarrow=False, yshift=10)
        #fig.add_annotation(x=1963, y=5.21875, text="Lowest Recorded Interest Rate for Nigeria in 1963", showarrow=False, yshift=-15)
        #fig.show()
        st.plotly_chart(fig)
        
    
