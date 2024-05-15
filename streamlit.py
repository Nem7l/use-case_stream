import streamlit as st

def main():
    st.title("My Job Posting App")
    st.image('Shutterstock_1248459142.jpg', use_column_width=True) 
    st.image('Q1-1.png', use_column_width=True)
    st.image('Q1-2.png', use_column_width=True)
    st.image('Q2.png', use_column_width=True)
    st.image('Q3-1.png', use_column_width=True)
    st.image('Q3-2.png', use_column_width=True)

    # Add a plot or visualization
    st.subheader("Data Visualization")
    data = [1, 2, 3, 4, 5]
    st.line_chart(data)

# Run the app
if __name__ == "__main__":
    main()
