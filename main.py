# Import the required libraries
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Configure Streamlit app with a modern UI
st.set_page_config(page_title="Data Sweeper", layout="wide")

# Apply a sleek, modern UI theme with enhanced design
st.markdown(
    """
    <style>
        body {
            background-color: #0d1117;  # Set background color
            color: #c9d1d9;  # Set text color
            font-family: 'Inter', sans-serif;  # Use a modern font
        }
        .block-container {
            padding: 2rem;  # Set padding
            border-radius: 16px;  # Add rounded corners
            background-color: #161b22;  # Set container background
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);  # Add shadow effect
        }
        h1, h2, h3, h4, h5, h6 {
            color: #58a6ff;  # Set header color
        }
        .stButton>button {
            border: none;  # Remove border
            border-radius: 12px;  # Add rounded corners to button
            background: linear-gradient(90deg, #0078D7, #005a9e);  # Apply gradient
            color: white;  # Set text color
            padding: 10px 20px;  # Add padding
            font-size: 1rem;  # Set font size
            transition: all 0.3s ease-in-out;  # Add transition effect
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #005a9e, #003f7f);  # Hover gradient
            transform: scale(1.05);  # Slightly enlarge button on hover
        }
        .stDataFrame, .stTable {
            border-radius: 12px;  # Add rounded corners to data tables
            overflow: hidden;  # Prevent overflow
            background-color: #21262d;  # Set table background
            color: #c9d1d9;  # Set table text color
        }
        .stDownloadButton>button {
            background: linear-gradient(90deg, #28a745, #218838);  # Set download button gradient
            border-radius: 12px;  # Add rounded corners to download button
            color: white;  # Set text color
            padding: 10px 20px;  # Add padding
            transition: all 0.3s ease-in-out;  # Add transition effect
        }
        .stDownloadButton>button:hover {
            background: linear-gradient(90deg, #218838, #1c6d32);  # Hover gradient
            transform: scale(1.05);  # Slightly enlarge button on hover
        }
    </style>
    """,
    unsafe_allow_html=True  # Allow HTML styling
)

# Set the title of the Streamlit app
st.title("🚀 Advanced Data Sweeper")

# Add a brief description of the app
st.write("Transform and clean your data with ease while enjoying a modern UI experience.")

# Allow users to upload multiple CSV or Excel files
uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

# Check if any files have been uploaded
if uploaded_files:
    for file in uploaded_files:
        # Determine the file extension
        file_extension = os.path.splitext(file.name)[-1].lower()

        # Read the uploaded file into a DataFrame based on its extension
        df = pd.read_csv(file) if file_extension == ".csv" else pd.read_excel(file)
        
        # Display the file name and size
        st.write(f"**📄 File:** {file.name} ({file.size / 1024:.2f} KB)")

        # Show the first few rows of the DataFrame
        st.dataframe(df.head())
        
        # Add a subheader for data cleaning options
        st.subheader("🛠 Data Cleaning")

        # Provide an option to clean the data for the current file
        if st.checkbox(f"Clean Data ({file.name})"):

            # Button to remove duplicate rows from the data
            if st.button("Remove Duplicates"):
                df.drop_duplicates(inplace=True)
                st.write("✅ Duplicates Removed!")

            # Button to fill missing values in the data
            if st.button("Fill Missing Values"):
                df.fillna(df.mean(), inplace=True)
                st.write("✅ Missing Values Filled!")
        
        # Add a subheader for file conversion and download
        st.subheader("🔄 Convert & Download")

        # Allow users to choose the file format for conversion
        conversion_type = st.radio("Convert to:", ["CSV", "Excel"], key=file.name)

        # Button to convert the data and provide a download link
        if st.button("Convert & Download"):
            buffer = BytesIO()  # Create a buffer to store the file

            # Generate the output file name based on the chosen format
            file_name = file.name.replace(file_extension, ".csv" if conversion_type == "CSV" else ".xlsx")

            # Set the MIME type based on the chosen format
            mime_type = "text/csv" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            # Save the DataFrame to the buffer in the chosen format
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
            else:
                df.to_excel(buffer, index=False, engine='openpyxl')  # Use openpyxl for Excel
            buffer.seek(0)  # Reset buffer position

            # Provide a download button for the converted file
            st.download_button("⬇ Download File", data=buffer, file_name=file_name, mime=mime_type)

# Show a success message once all files are processed
st.success("🎉 Your files are ready!")

    # For displaying the Author's name
st.write("✨ Built by [Muhammad Talha](https://github.com/Muhammad-Talhas) ✨")
