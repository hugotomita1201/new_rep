import streamlit as stv

st.header('Tossing a Coin')

st.header('Tossing a coin')

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button: 
    st.write(f'Running the experiment of {number_of_trials} trials.')

st.write('It is not a functional application yet. Under construction.') 