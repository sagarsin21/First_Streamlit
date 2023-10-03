import streamlit as st
import pandas as pd

def main():
    st.title("Streamlit Excel Data Entry")

    # Get user input
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:")
    email = st.text_input("Enter your email:")

    # Create a DataFrame with the user input
    data = {'Name': [name], 'Age': [age], 'Email': [email]}
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.write("Entered Data:", df)

    # Add a submit button
    if st.button("Submit"):
        # Write the data to an Excel file
        df.to_excel("user_data.xlsx", index=False)
        st.success("Data submitted successfully!")
        if __name__ == "__main__":
    main()
