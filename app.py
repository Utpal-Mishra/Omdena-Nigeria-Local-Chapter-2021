import home
import one 
import two
import three
import four
import five
import interestrate
import mmi

import streamlit as st

st.audio(open('sweet.mp3', 'rb').read(), format='audio/ogg')

PAGES = {
    "Home": home,
    "Check Economic Crisis Status": one,
    "Visualize the Change in Interest Rate": interestrate,
    "Visualize Money Market Indicator": mmi,
    "Check Bank Account Eligibility": five,
    "Check Credit Card Eligibility": two,
    "Check Student Loan Status": three,
    "Check Employee Loan Status": four
}

st.sidebar.title('Navigation Bar')

selection = st.sidebar.selectbox("Go to: \n", list(PAGES.keys()))
page = PAGES[selection]
page.app()