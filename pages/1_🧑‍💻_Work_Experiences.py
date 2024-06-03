import streamlit as st
import json

st.header("Work Experience",divider='rainbow')

st.markdown("""
    <style>
    	[data-testid='stAppViewContainer'] {
    		background-color: #f9f9f9;
			opacity: 1;
			background-image: radial-gradient(#f7ca45 2px, #f9f9f9 2px);
			background-size: 40px 40px;
			background-position: top left;
			background-attachment: fixed;
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

def add_space(word1, word2):
	tot = 150
	print(len(word1), len(word2))
	return tot - len(word1) - len(word2)

def display_work_experience(entry):
	space = "&nbsp;" * 3

	with st.expander(f"{entry['title']}, {space} {entry['duration']}", expanded=True):
		st.write(f"[{entry['company']}]({entry['company_link']}), {space} {entry['location']}")
		st.write(entry["description"])

		if len(entry['links']) > 0:
			for l in entry['links']:
				print(l.keys())
				st.write(f"[{list(l.keys())[0]}]({list(l.values())[0]})")


# Read in Data
with open("data/work_exp.json", "r") as f:
	work_exp = json.load(f)

# Print out each entity
for entry in work_exp:
	display_work_experience(entry)