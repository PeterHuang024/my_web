import streamlit as st
import base64

st.set_page_config(page_title="TYHuang's Web", layout="wide", page_icon='⭐️')

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

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("images/bg.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-attachment: fixed;
        background-position: top left;
        opacity: 0.75; /* Adjust the opacity value for transparency */
    }}
    .middle-text {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 36px;
        text-align: center;
    }}

    [data-testid="stHeader"] {{
	background: rgba(0,0,0,0);
	}}

    </style>
    """,
    unsafe_allow_html=True
)


st.title("Hi! I'm Peter")
st.write("Experienced Data Scientist with a track record in the tech and aviation industries.")
st.write("Proficient in Data Science, A/B testing, Machine Learning, Data Modeling & ETL, and Analytics & Visualization.") 
st.write("#Data Science #Analytics #Machine Learning")