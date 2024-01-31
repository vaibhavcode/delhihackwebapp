import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.app_logo import add_logo 

st.set_page_config(page_title='Webapp', page_icon='😁', layout="wide", initial_sidebar_state="auto")
add_logo('https://icons.iconarchive.com/icons/hopstarter/3d-cartoon-vol3/128/Axialis-Icon-Workshop-Classic-icon.png')
st.sidebar.markdown('_by team xyz_')


tab1, tab2, tab3, tab4 = st.tabs(["Hindi", 'English', 'Punjabi', 'Bengali'])


st.columns(3)[1].header("Project Name")

add_vertical_space(5)

col1, col2 = st.columns(2, gap='large')

with col2:
    st.markdown('### Heading')
    st.markdown('Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.')

with col1:
    st.video('https://youtu.be/MWi-WbFGkgg')


with st.expander("See More"):
    st.write('lolzers')
