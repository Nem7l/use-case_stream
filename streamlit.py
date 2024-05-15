import streamlit as st

def main():

    st.title("My Jop Posting APP")


  
        st.image('https://craresources.com/wp-content/uploads/2022/07/Shutterstock_1248459142-job-search.jpg', use_column_width=True)
    
    name = st.text_input("Enter your name", "")

   
    if st.button("Submit"):
        st.write(f"Hello, {name}!")

    # Add a plot or visualization
    st.subheader("Data Visualization")
    data = [1, 2, 3, 4, 5]
    st.line_chart(data)

 

# Run the app
if __name__ == "__main__":
    main()
