import streamlit as st
import json

st.header("Articles",divider='rainbow')

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

st.subheader('Sharing my journey in Data Science, more will come!!')

st.markdown("### Medium:")
st.markdown("- 美國Data求職經歷：實習、正職、Layoff再上岸")
st.link_button('Full Article', 'https://medium.com/@kobe24abc/%E7%BE%8E%E5%9C%8Bdata%E6%89%BE%E5%B7%A5%E7%B6%93%E6%AD%B7-%E5%AF%A6%E7%BF%92-%E6%AD%A3%E8%81%B7-layoff%E5%86%8D%E4%B8%8A%E5%B2%B8-e1b4ac455068')

st.markdown("- Syracuse University M.S. Applied Data Science 讀書心得")
st.link_button('Full Article', 'https://medium.com/@kobe24abc/syracuse-university-m-s-applied-data-science-%E8%AE%80%E6%9B%B8%E5%BF%83%E5%BE%97-d98bee36f85c')

st.markdown("- Data 美國找工資源分享")
st.link_button('Full Article', 'https://medium.com/@kobe24abc/data-%E7%BE%8E%E5%9C%8B%E6%89%BE%E5%B7%A5%E8%B3%87%E6%BA%90%E5%88%86%E4%BA%AB-46d792c5c90c')

st.markdown("Streamlit: Data Science App的好工具")
st.link_button("https://medium.com/@kobe24abc/streamlit-data-science-app%E7%9A%84%E5%A5%BD%E5%B7%A5%E5%85%B7-5802a0dde498")

################

st.markdown("### Publications:")
st.markdown("- A computational analysis of accessibility, readability, and explainability of figures in open access publications")
st.link_button('Full Article', 'https://epjds.epj.org/articles/epjdata/abs/2023/01/13688_2023_Article_380/13688_2023_Article_380.html')

st.markdown("- Graphical integrity issues in open access publications: Detection and patterns of proportional ink violations")
st.link_button('Full Article', 'https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009650')

st.markdown("- Data analysis of the risks of type 2 diabetes mellitus complications before death using a data-driven modelling approach: methodologies and challenges in prolonged diseases")
st.link_button('Full Article', 'https://www.mdpi.com/2078-2489/12/8/326')


