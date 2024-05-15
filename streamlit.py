import streamlit as st

def main():

    st.title("My Jop-posting app")


    st.header("Header")
    st.subheader("Subheader")

    
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
