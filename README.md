# MovieRecommender
Recommends movies from TMDB top 5000. Uses content based recommender system.
Dataset taken from Kaggle

# Initialisation & Running

extract `tmdb_5000_credits.zip` first. It was zipped as GitHub doesn't allow files larger than 25MB.

Run the `Analysis code.ipynb` first. This will pickle dump some stuff

(I used python 3.12.1)
Please create a virtual environment (venv) in your folder and then to install streamlit.
Then in your terminal,
install `pip install streamlit`
run `streamlit run app.py`
or `python -m streamlit run app.py`

To run the improved GUI:
run `streamlit run app_final.py`
or `python -m streamlit run app_final.py`

Click on the address given in your terminal, or streamlit might automatically open
