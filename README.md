How to Run the Streamlit Dashboard via Ngrok

1. **Start the Streamlit Dashboard:**
   Open your terminal and run the dashboard app:
   ```bash
   streamlit run dashboard.py
Configure Ngrok (First time only):

Create a free account on Ngrok Dashboard.

Copy your Authtoken from your ngrok account.

Authenticate your ngrok agent in the terminal by running:

Bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
Expose the Dashboard Publicly:
Run ngrok to map port 8501 to a public URL:

Bash
ngrok http 8501
