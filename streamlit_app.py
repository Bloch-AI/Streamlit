import streamlit as st

st.title("Main Cover Page")
st.write("Welcome to the main cover page. Select an app to navigate to:")

# List of other Streamlit apps with their URLs
apps = {
    "App 1": "https://blochai-machinelearning.streamlit.app/",
    "App 2": "https://blochai-processmining.streamlit.app/",
}

for app_name, app_url in apps.items():
    st.markdown(f"[{app_name}]({app_url})")

st.write("Click the links above to navigate to the respective apps.")

# Add footer
st.markdown('<div class="footer"><p>© 2024 Bloch AI LTD - All Rights Reserved. <a href="https://www.bloch.ai" style="color: black;">www.bloch.ai</a></p></div>', unsafe_allow_html=True)
