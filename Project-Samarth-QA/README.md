
# Project-Samarth-QA (Minimal Demo)

Demo prototype for Project Samarth: a simple question-answering system over two sample datasets (rainfall and crop production).
This is a minimal runnable prototype to demonstrate end-to-end flow: question -> backend query planner -> answer with dataset provenance.

## Run locally (recommended)
1. Create a virtual env and install:
   ```
   pip install -r requirements.txt
   ```
2. Run Streamlit app:
   ```
   streamlit run frontend/app.py
   ```
3. Try these sample questions:
   - `Compare average rainfall in Bihar and Jharkhand for the last 2 years`
   - `Identify the district in Bihar with the highest production of Rice`

## Files
- `data/` : sample CSVs used by demo
- `backend/etl.py` : simple loaders & normalizers
- `backend/query_planner.py` : tiny rule-based parser + answer functions
- `frontend/app.py` : Streamlit UI
- `requirements.txt` : minimal deps

## Notes
- This is a minimal educational prototype. For full Project Samarth you'd add data.gov.in discovery, richer NL parsing, normalization of state/district codes, caching, and deployment.
