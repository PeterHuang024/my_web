import streamlit as st
import json

st.header("Education",divider='rainbow')

st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #FFF8DC;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
	st.image("images/linkedin_icon.png", use_column_width=True)
	st.title("""Tzu-Yang (Peter) Huang""")
	st.markdown("- Data Scientist")