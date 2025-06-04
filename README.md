# Streamlit web interface with prediction using trained Linear Regression model

This is a simple AI-powered web app using Streamlit, demonstrating a linear regression model prediction.

## Features

- Input a number
- Predict using a pre-trained Linear Regression model
- See results instantly in browser

## Project Structure

```
streamlit_ai_app/
├── streamlit_app.py         # Main Streamlit app
├── requirements.txt         # Python dependencies
├── model.pkl                # Pre-trained model
└── README.md                # Project guide
```

## How to Deploy

1. Fork or clone this repository.
2. Push to your public GitHub.
3. Go to [Streamlit Cloud](https://streamlit.io/cloud)
4. Click **"New app"**
5. Choose your repo, set main file to `streamlit_app.py`, click **Deploy**

## Local Run (Optional)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Notes

- This demo runs a simple `LinearRegression` model trained on `[1, 2, 3, 4] => [2, 4, 6, 8]`.
- Suitable for deployment on Streamlit Community Cloud (free tier).
