import streamlit as st

def main():
    st.set_page_config(page_title="My Job Posting App", layout="wide")

  
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="font-weight: bold;">My Job Posting App</h1>
            <p>Explore the dynamic job market in Saudi Arabia</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  
    st.image("Shutterstock_1248459142-job-search-2.jpg", use_column_width=True)

    
    st.write("")

    
    st.markdown(
        """
        ## Jobs in Saudi Arabia
        Saudi Arabia offers a wide range of job opportunities across various industries and sectors, reflecting a vibrant and diverse job market.
        """
    )

    
    st.markdown(
        """
        ## Regional Job Market
        The picture depicts job postings in Saudi Arabia, specific to each region, indicating a diverse and segmented job market.
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.image("Q1-1.png", use_column_width=True)
    with col2:
        st.image("Q1-2.png", use_column_width=True)

    
    st.markdown(
        """
        ## Gender Preference
        The graph highlights a significant change in the job market, where opportunities are presented without any gender preference.
        """
    )
    st.image("Q2.png", use_column_width=True)

    
    st.markdown(
        """
        ## Salary Range for Recent Graduates
        The picture illustrates the expected salary for recent graduates, in ranges between 3000-12000 SAR, with the majority falling within the 4000-7000 SAR range.
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.image("Q3-1.png", use_column_width=True)
    with col2:
        st.image("Q3-2.png", use_column_width=True)

    
    st.markdown(
        """
        ## Job Opportunities
        Job opportunities cater to both experienced professionals and fresh graduates, as shown in the graph below, with a higher preference for freshly graduated students.
        """
    )
    st.image("Q4.png", use_column_width=True)

    st.markdown(
        """
        ##  Job opportunities salary can differ from city to another with the maximum salary in Riyadh as you can see in the chart below
        """
    )
    st.image("Q4.png", use_column_width=True)
    
if __name__ == "__main__":
    main()
