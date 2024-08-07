import streamlit as st

st.title("💻 Here's one I made earlier! 🌈")
st.title("")
st.title("Select one of Jamie's apps:")

# List of other Streamlit apps with their URLs
apps = {
    "Machine Learning": "https://blochai-machinelearning.streamlit.app/",
    "Process Mining": "https://blochai-processmining.streamlit.app/",
}

for app_name, app_url in apps.items():
    st.markdown(f"[{app_name}]({app_url})")

st.write("")

# Add footer
st.markdown('<div class="footer"><p>© 2024 Bloch AI LTD - All Rights Reserved. <a href="https://www.bloch.ai" style="color: black;">www.bloch.ai</a></p></div>', unsafe_allow_html=True)
