import streamlit as st
import pandas as pd

# Data for "Correct Score - Odds"
correct_score_data = {
    "Score": ["1:0", "2:0", "2:1", "3:0", "3:1", "3:2", "4:0", "4:1", "5:0",
              "0:0", "1:1", "2:2", "3:3", "4:4", "5:5", "other",
              "0:1", "0:2", "1:2", "0:3", "1:3", "2:3", "0:4", "1:4", "0:5"],
    "Odds": [4.36, 7.50, 9.70, 20, 25, 65, 68, 88, None,
             5.00, 5.60, 25, None, None, None, None,
             6.50, 17, 15, 65, 56, 97, None, None, None]
}

# Data for "Half Time / Full Time - Odds"
ht_ft_data = {
    "HT/FT": ["1/1", "1/X", "1/2", "X/1", "X/X", "X/2", "2/1", "2/X", "2/2"],
    "Odds": [3.06, 18, 78, 4.37, 3.48, 7.30, 48, 18, 6.00]
}

# Streamlit App
st.title("Betting Odds and Probabilities")

# Correct Score - Odds Table
st.subheader("Correct Score - Odds")
correct_score_df = pd.DataFrame(correct_score_data)
st.dataframe(correct_score_df, use_container_width=True)

# Half Time / Full Time - Odds Table
st.subheader("Half Time / Full Time - Odds")
ht_ft_df = pd.DataFrame(ht_ft_data)
st.dataframe(ht_ft_df, use_container_width=True)
