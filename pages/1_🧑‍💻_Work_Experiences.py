import streamlit as st
import json

st.header("Work Experience",divider='rainbow')

with st.sidebar:
	st.image("images/linkedin_icon.png", use_column_width=True)
	st.title("""Tzu-Yang (Peter) Huang""")
	st.markdown("- Data Scientist")

def add_space(word1, word2):
	tot = 150
	print(len(word1), len(word2))
	return tot - len(word1) - len(word2)

def display_work_experience(entry):
	space1 = "&nbsp;" * entry['space1']
	space2 = "&nbsp;" * entry['space2']

	with st.expander(f"{entry['title']} {space1} {entry['duration']}", expanded=True):
		st.write(f"[{entry['company']}]({entry['company_link']}) {space2} {entry['location']}")
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