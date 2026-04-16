import streamlit as st
st.set_page_config(page_title="Research Agent")
import requests

st.title("Research Agent")
st.write("Ask anything — the agent will search the web and summarize for you.")

query = st.text_input("Enter your research query:")

if st.button("Research"):
    if query:
        with st.spinner("Agent is researching..."):
            response = requests.post(
                "https://Trolling-Kakashi-research-agent.hf.space/analyze",
                json={"query": query}
            )
            if response.status_code == 200:
                st.markdown(response.json()["result"])
            else:
                st.error("Something went wrong. Try again.")
    else:
        st.warning("Please enter a query first.")
