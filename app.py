import streamlit as st
import pandas as pd
import requests

st.title("🏏 Live Cricket Score")

url = "https://api.cricapi.com/v1/currentMatches?apikey=09a82d34-1169-435f-896a-ab8d33ce56de"

response = requests.get(url)

# Check response
if response.status_code == 200:
    data = response.json()

    # Debug (dekhne ke liye kya aa raha hai)
    st.write("API Response:", data)

    matches = []

    # Safe access
    if 'data' in data:
        for match in data['data']:
            matches.append({
                "Match": match.get('name', 'N/A'),
                "Status": match.get('status', 'N/A')
            })

        if matches:
            df = pd.DataFrame(matches)
            st.write(df)
        else:
            st.warning("No matches found")
    else:
        st.error("API me 'data' nahi mila")
        st.write(data)

else:
    st.error("API request failed")
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
