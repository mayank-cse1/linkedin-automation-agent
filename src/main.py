
from llm.gemini_client import get_structured_job_description
from utils.job_link_text_extraction import extract_text_from_url
from utils.linkedin_post import linkedin_post_creation
from utils.linkedin_posting import post_to_linkedin

if __name__ == "__main__":
    url = input("Enter the article URL: ")
    extracted_text = extract_text_from_url(url)

    if extracted_text:
        structured_content = get_structured_job_description(extracted_text)
        print("\nGenerated LinkedIn Post:\n", structured_content)
        post_content = linkedin_post_creation(structured_content, url)
        post_to_linkedin(post_content)

    else:
        print("❌ Failed to extract text from the URL.")
