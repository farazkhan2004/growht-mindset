import streamlit as st 

st.set_page_config(page_title="Self Growth Mindset",page_icon="")
st.title(""" GROWTH MINDSET MOTIVATION """)

st.markdown("This app help for your future!")

name=st.text_input("Enter your name")

age=st.text_input(f"Enter Age.")

goal= st.text_input("What's your goal in your life?")

if st.button("submit"):
    st.success(f"GOOD LUCK!{name} keep focused in your {goal}.") 
               
    st.write("""STRUGGLE IS THE MAIN THING TO GET BIG ACHIVEMENT IN YOUR LIFE.""")
else:
    st.info("Fix your goal")