import streamlit as st
import json

st.header("Education",divider='rainbow')

st.markdown("""
    <style>
    	[data-testid='stAppViewContainer'] {
    		background-color: #f9f9f9;
			opacity: 1;
			background-image: radial-gradient(#f7ca45 2px, #f9f9f9 2px);
			background-size: 40px 40px;
    	}
        [data-testid=stSidebar] {
            background-color: #FFF8DC;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
	st.image("images/photo.png", use_column_width=True)
	st.title("""Tzu-Yang (Peter) Huang""")
	st.markdown("- Data Scientist")

col1, col2, col3 = st.columns([2,0.5,1])
with col1:
	st.subheader(f"[Syracuse University, iSchool](https://ischool.syr.edu/)")
	
with col3:
	st.subheader("Syracuse, NY")
	
col1, col2, col3 = st.columns([2,0.5,1])
with col1:
	st.markdown("#### M.S. Applied Data Science")
with col3:
	st.markdown("#### 2020 ~ 2022")

st.markdown('- Teaching Assistant in IST718: Big Data Analytics Course')
st.divider()

col1, col2, col3 = st.columns([2,0.5,1])
with col1:
	st.subheader(f"[National Chengchi University](https://www.nccu.edu.tw)")
	
with col3:
	st.subheader("Taipei, Taiwan")
	
col1, col2, col3 = st.columns([2,0.5,1])
with col1:
	st.markdown("#### B.S. Mathematical Sciences")
with col3:
	st.markdown("#### 2015 ~ 2019")



