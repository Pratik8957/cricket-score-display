import streamlit as st
import pandas as pd
import requests

# Page config
st.set_page_config(page_title="Live Cricket Score", page_icon="🏏", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>🏏 Live Cricket Score</h1>", unsafe_allow_html=True)

# API URL
API_KEY = "09a82d34-1169-435f-896a-ab8d33ce56de"
URL = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}"

# Cache data to avoid API blocking
@st.cache_data(ttl=60)
def fetch_matches():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "error", "reason": "API request failed"}
    except:
        return {"status": "error", "reason": "Connection error"}

data = fetch_matches()

# UI Section
st.markdown("### 📊 Live Matches")

# Handle API errors
if data.get("status") == "failure":
    st.error(f"❌ API Error: {data.get('reason')}")
    st.info("⏳ Please wait a few minutes and refresh.")

elif "data" in data:

    matches = []

    for match in data["data"]:
        matches.append({
            "🏟 Match": match.get("name", "N/A"),
            "📌 Status": match.get("status", "N/A")
        })

    if matches:
        df = pd.DataFrame(matches)

        # Display styled table
        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No live matches available right now.")

else:
    st.error("⚠️ Unexpected API response")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
# import streamlit as st
# import pandas as pd
# import requests

# st.title("🏏 Live Cricket Score")

# url = "https://api.cricapi.com/v1/currentMatches?apikey=09a82d34-1169-435f-896a-ab8d33ce56de"

# response = requests.get(url)
# data = response.json()

# matches = []

# for match in data['data']:
#     matches.append({
#         "Match": match['name'],
#         "Status": match['status']
#     })

# df = pd.DataFrame(matches)

# st.write(df)
