import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>My Job Posting App</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        body {
            background-image: url('Shutterstock_1248459142-job-search-2.jpg');
            background-repeat: no-repeat;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.image('Q1-1.png', use_column_width=True)
    st.image('Q1-2.png', use_column_width=True)
    st.image('Q2.png', use_column_width=True)
    st.image('Q3-1.png', use_column_width=True)
    st.image('Q3-2.png', use_column_width=True)


if __name__ == "__main__":
    main()
