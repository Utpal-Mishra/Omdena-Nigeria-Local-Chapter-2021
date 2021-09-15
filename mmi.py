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
    data = data.sort_values(by=['Month', 'Year'])
    data = data.reset_index().drop(["index"], axis = 1)
    
    
    print("BEFORE: Total Empty Values in the Dataset: {}".format(data.isna().sum().sum()))
    data = data.fillna(data.mean(axis = 0))
    print("AFTER : Total Empty Values in the Dataset: {}".format(data.isna().sum().sum()))
    
    st.write(data)
        
    st.write("")
    st.write("")
    
        
    if st.checkbox("InterBank Call Rate"):   
        fig = px.bar(data, x="Month", y="InterBankCallRate", text = "InterBankCallRate", animation_frame = "Year", color='InterBankCallRate', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("Treasury Bill Rate"):   
        fig = px.bar(data, x="Month", y="TreasuryBill", text = "TreasuryBill", animation_frame = "Year", color='TreasuryBillx', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("Savings Deposits Rate"):   
        fig = px.bar(data, x="Month", y="SavingsDeposit", text = "SavingsDeposit", animation_frame = "Year", color='SavingsDeposit', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("One Month Deposit Rate"):   
        fig = px.bar(data, x="Month", y="OneMonthDeposit", text = "OneMonthDeposit", animation_frame = "Year", color='OneMonthDeposit', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("Three Months Deposit Rate"):   
        fig = px.bar(data, x="Month", y="ThreeMonthsDeposit", text = "ThreeMonthsDeposit", animation_frame = "Year", color='ThreeMonthsDeposit', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("Six Months Deposit Rate"):   
        fig = px.bar(data, x="Month", y="SixMonthsDeposit", text = "SixMonthsDeposit", animation_frame = "Year", color='SixMonthsDeposit', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)
        
    if st.checkbox("Twelve Months Deposit Rate"):   
        fig = px.bar(data, x="Month", y="TwelveMonthsDeposit", text = "TwelveMonthsDeposit", animation_frame = "Year", color='TwelveMonthsDeposit', barmode='group')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text = "Year", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Money Market Indicator", showline=True, linewidth=2, linecolor='black', mirror=True)
        #fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1000, title_text="Money Market Indicator of Nigeria from 1960-2020") 
        #fig.show()
        st.plotly_chart(fig)

       
    df = data.melt(id_vars=["Year", "Month"], var_name = "MMI", value_name = "Percent (%)")
    df.sort_values(["Month", "Year"], inplace = True)
    df = df.reset_index().drop(["index"], axis = 1)
      
    if st.checkbox("Money Market Indicator"):
        fig = px.scatter(df, x="Month", y="Percent (%)", animation_frame="Year", size=df["Percent (%)"], color="Percent (%)", hover_name="Year", facet_col="Month")
        fig.update_xaxes(title_text = "Months", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "Percent (%)", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1600, title_text="Money Market Indicator of Nigeria from 1960 - 2020") 
        #fig.show()
        st.plotly_chart(fig)
    
