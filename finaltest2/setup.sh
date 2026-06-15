#!/bin/bash
# Streamlit configuration setup script for Heroku deployment

mkdir -p ~/.streamlit

echo "[general]
email = \"your-email@domain.com\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
enableCORS = false
enableXsrfProtection = true
maxUploadSize = 200
port = \$PORT

[client]
showErrorDetails = false
toolbarMode = \"minimal\"

[logger]
level = \"info\"

[browser]
gatherUsageStats = false

[theme]
primaryColor = \"#1f77b4\"
backgroundColor = \"#ffffff\"
secondaryBackgroundColor = \"#f0f2f6\"
textColor = \"#262730\"
font = \"sans serif\"
" > ~/.streamlit/config.toml

echo "✅ Streamlit configuration completed successfully!"
