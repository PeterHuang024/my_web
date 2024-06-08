import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time

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

# Add a title for the Contact Me form
st.title("Contact Me")


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
def read_data():
    return conn.read(worksheet="sheet1", usecols=[0, 1, 2], ttl="0")

# Read existing data from the Google Sheets
df = read_data()
#df = conn.read(worksheet="sheet1", usecols=[0, 1, 2], ttl="10m")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
    	new_row = {'Name':name, 'Email':email, 'Message': message}
    	min_idx = df.isnull().all(axis=1).idxmax()
    	try:
    		df.loc[min_idx] = new_row
    		conn.update(data = df)
    		st.success(f"Thank you, {name}! Your message has been received.")
    		time.sleep(10)
    		st.experimental_rerun()

    	except Exception as e:
    		st.error(f"Failed to send message. Error: {e}")

        
