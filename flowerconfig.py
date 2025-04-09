import os

# Read configuration from environment variables
auth_provider = "flower.views.auth.GoogleAuth2LoginHandler"
auth = os.environ.get("FLOWER_AUTH_PATTERN", "allowed-emails.*@orbio.work")
oauth2_key = os.environ.get("FLOWER_OAUTH2_KEY")
oauth2_secret = os.environ.get("FLOWER_OAUTH2_SECRET")
oauth2_redirect_uri = os.environ.get("FLOWER_OAUTH2_REDIRECT_URI", "http://localhost:5555/login")
