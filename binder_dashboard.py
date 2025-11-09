import streamlit as st
import os

st.set_page_config(page_title="AI Land & Mineral Intelligence — Binder Dashboard", layout="wide")

st.title("AI Land & Mineral Intelligence — Binder Dashboard")
st.markdown("Welcome, **Michael Carey** — Founder & Human Lead.")

# Sidebar sections
sections = [
    "Administrative_&_Governance",
    "Family_&_Legacy",
    "Homeland_&_Infrastructure",
    "Legal_&_Compliance_System",
    "Vision_&_Evolution"
]

selected = st.sidebar.selectbox("Binder Sections", sections)

# Show section contents if folder exists
base_path = "."
section_path = os.path.join(base_path, selected)

st.header(selected.replace("_", " "))

if os.path.isdir(section_path):
    files = [f for f in os.listdir(section_path) if os.path.isfile(os.path.join(section_path, f))]
    if files:
        selected_file = st.selectbox("Select a document", files)
        with open(os.path.join(section_path, selected_file), "r", encoding="utf-8") as f:
            st.text_area("File Preview", f.read(), height=400)
    else:
        st.info("This folder is currently empty.")
else:
    st.warning("Folder not found. Create folders in your GitHub repo matching the section names above.")

st.markdown("---")
st.markdown("© 2025 Michael Carey — Founder, AI Land & Mineral Intelligence | Contact: aiLandMinerals.invest@gmail.com (Founder inquiries only)")
st.markdown("_Created under the direction and human lead of Michael Carey — AI-assisted under his instruction._")