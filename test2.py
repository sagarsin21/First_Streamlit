import streamlit as st
import pandas as pd

def main():
    st.title("Streamlit Login and Data Export App")

    # Input for username
    username = st.text_input("Username:")

    # Input for password (password input field for security)
    password = st.text_input("Password:", type="password")

    # Submit button
    if st.button("Submit"):
        # Check if the username and password are not empty
        if username and password:
            # Export data to Excel
            export_data_to_excel(username, password)
            st.success("Data exported to Excel successfully!")
        else:
            st.error("Please enter both username and password.")

def export_data_to_excel(username, password):
    # Example: Creating a Pandas DataFrame with the input data
    data = {'Username': [username], 'Password': [password]}
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel('user_data.xlsx', index=False)

if __name__ == "__main__":
    main()
