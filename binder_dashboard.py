import os
import streamlit as st

# Set the base path for your Binder
base_path = os.path.join(os.path.expanduser("~"), "Documents", "AI_Land_&_Mineral_Intelligence_Binder_v2_1")

# Page title
st.title("AI Land & Mineral Intelligence — Binder Dashboard")
st.write("Welcome, Michael Carey — Founder & Human Lead.")

# Sidebar with folders
folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
selected_folder = st.sidebar.selectbox("Binder Sections", folders)

folder_path = os.path.join(base_path, selected_folder)
files = os.listdir(folder_path)

st.header(selected_folder)
if not files:
    st.info("This folder is currently empty.")
else:
    for f in files:
        st.write(f"📄 {f}")
        file_path = os.path.join(folder_path, f)
        if f.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            st.text_area(f"Contents of {f}", content, height=150)