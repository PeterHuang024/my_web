import streamlit as st
import json

st.header("Skills",divider='rainbow')

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

skill_set = {'Programming Language':['Python', 'SQL', 'R Programming', 'Pyspark'],
			 'Cloud Platforms & Services': ['AWS SageMaker', 'AWS Cloud9', 'Databricks', 'Azure DevOps'],
			 'Database & Storage':['AWS Redshift', 'Oracle RDBMS', 'MSSQL', 'AWS S3', 'DB Delta Lake', 'HDFS'],
			 'Visualiztions':['Tableau', 'Power BI', 'Matplotlib', 'Seaborn'],
			 'Version Control':['Git', 'GitHub', 'AWS CodeCommit'],
			 'Other Tools': ['Docker', 'MS Excel', 'MS PowerPoint', 'MS Word']}

for k in list(skill_set.keys()):
	st.markdown("### " + k)
	columns = st.columns(6)

	for i in range(6):
		try:
			columns[i].button(skill_set[k][i])
		except:
			break