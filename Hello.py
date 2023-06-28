import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(page_title="TYHuang's Web", layout="wide", page_icon='😇')

with st.sidebar:
	st.write("👋"+"""Welcome to my personal website! I'm Peter (Tzu-Yang), a passionate data scientist who enjoys learning and implementing cutting-edge methodologies to tackle complex problems. 
					 Currently, I am an Analytics & Insights Professional at Amazon Advertising, where I thrive on leveraging data to drive impactful solutions. 
					 Feel free to explore my website to learn more about my work and projects.""")
	col1, col2 = st.columns([1, 10])
	with col1:
		st.image('./images/linkedin_icon.png', width=25)
	with col2:
		st.markdown('[Linkedin](https://www.linkedin.com/in/tyanghuang)')


with open('timeline.json', "r") as f:
    timeline_data = f.read()
        
timeline(timeline_data, height=600)

# render timeline

st.subheader('Skills')
st.markdown('- **Programming Languages**: Python, R, SQL, T-SQL')
st.markdown('- **Database and Storage**: MSSQL, Oracle Database, S3, Redshift')
st.markdown('- **Software & Tools**: PySpark, Docker, AWS, Azure, Hadoop, SSRS, Git, Tableau, Power BI, Power Apps, MS Excel, CodeCommit')

st.subheader('Publications')
st.markdown("""- [A computational analysis of accessibility, readability, and explainability of figures in open access publications](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-023-00380-y)
				, Mar 2023  \n Han Zhung, Tzu-Yang Huang, Daniel E. Acuna, EPJ Data Science""")
st.markdown("""- [Graphical integrity issues in open access publications: detection and patterns of proportional ink violations](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009650)
				, Dec 2021  \n Han Zhung, Tzu-Yang Huang, Daniel E. Acuna, PLOS Computational Biology""")