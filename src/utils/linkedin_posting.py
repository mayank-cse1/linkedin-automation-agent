import requests

import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# LinkedIn API Credentials
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
USER_PROFILE = os.getenv("PROFILE_URN")
USER_URN = f"urn:li:person:{USER_PROFILE}"  # Construct the LinkedIn Profile URN

# LinkedIn API Endpoint
LINKEDIN_URL = "https://api.linkedin.com/v2/ugcPosts"

# Headers for LinkedIn API
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}
def post_to_linkedin(content):
    """Posts content to LinkedIn using API."""
    payload = {
        "author": USER_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(LINKEDIN_URL, headers=HEADERS, json=payload)

    if response.status_code == 201:
        print("✅ Successfully posted on LinkedIn!")
    else:
        print(f"❌ Error: {response.status_code}, {response.text}")