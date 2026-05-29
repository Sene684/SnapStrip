import streamlit as st
import replicate
import os

# --- Page Config ---
st.set_page_config(page_title="SnapStrip", page_icon="📸")
st.title("📸 SnapStrip")
st.write("Snap it. Strip it. Wear it.")

# --- API Configuration ---
# This looks for the key you saved in the Streamlit "Secrets" dashboard
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
else:
    st.error("API Token not found! Please set REPLICATE_API_TOKEN in Streamlit Secrets.")
    st.stop()

# --- User Interface ---
uploaded_files = st.file_uploader("Upload 4 photos for your comic strip", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

if uploaded_files and len(uploaded_files) == 4:
    if st.button("Generate Comic Strip"):
        st.write("Processing your photos...")
        
        # --- Logic Placeholder ---
        # This is where your Replicate model call will go
        # For now, we are just confirming the files were received
        st.success(f"Received {len(uploaded_files)} photos! Ready to send to Replicate.")
        
        # Example of how you'll call your model later:
        # output = replicate.run("your-model-path-here", input={"image": uploaded_files[0]})
        
elif uploaded_files:
    st.info(f"Please upload exactly 4 photos. You currently have {len(uploaded_files)}.")

# --- Footer ---
st.markdown("---")
st.write("SnapStrip v1.0 | Powered by Replicate & Zazzle")
