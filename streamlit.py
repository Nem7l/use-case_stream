import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>My Job Posting App</h1>", unsafe_allow_html=True)

    st.image('Shutterstock_1248459142-job-search-2', use_column_width=True)

    st.markdown("""Jobs in Saudi Arabia: Saudi Arabia offers a wide range of job opportunities across various industries and sectors, reflecting a vibrant and diverse job market.""")
    st.markdown("""Regional Job Market: The picture depicts job postings in Saudi Arabia, specific to each region, indicating a diverse and segmented job market.""")
    st.image('Q1-1.png', use_column_width=True)
    st.image('Q1-2.png', use_column_width=True)

    st.markdown("""The graph highlights a significant change in the job market, where opportunities are presented without any gender preference.""")
    st.image('Q2.png', use_column_width=True)

    st.markdown("""The picture illustrates the expected salary for recent graduates, which ranges between 3000-12000 SAR, with the majority falling within the 4000-7000 SAR range.""")
    st.image('Q3-1.png', use_column_width=True)
    st.image('Q3-2.png', use_column_width=True)

    st.markdown("""Job opportunities cater to both experienced professionals and fresh graduates, as shown in the graph below, with a higher preference for freshly graduated students.""")
    st.image('Q4.png', use_column_width=True)

if __name__ == "__main__":
    main()
