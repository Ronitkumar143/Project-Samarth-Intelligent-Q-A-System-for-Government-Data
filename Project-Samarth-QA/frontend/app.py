
import streamlit as st
from backend.query_planner import answer_question
st.set_page_config(page_title="Project Samarth - Demo QA", layout="centered")
st.title("Project Samarth — Demo Q&A (Sample Data)")
st.write("This is a lightweight demo. Ask: 'Compare average rainfall in Bihar and Jharkhand for the last 2 years' or 'Identify the district in Bihar with the highest production of Rice'")

question = st.text_input("Enter your question", value="Compare average rainfall in Bihar and Jharkhand for the last 2 years")
if st.button("Ask"):
    with st.spinner("Thinking..."):
        ans = answer_question(question)
    if isinstance(ans, dict) and "error" in ans:
        st.error(ans["error"])
    else:
        st.success("Answer generated (see details below)")
        st.json(ans)
        st.markdown("**Sources / Provenance**")
        for s in ans.get("sources", []):
            st.write(f'- {s["dataset"]} — `{s["path"]}`')
