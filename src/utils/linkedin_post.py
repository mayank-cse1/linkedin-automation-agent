def linkedin_post_creation(job_details, job_link):
    job_post = f"""
    🚀 # {job_details.company_name} Hiring! 🚀

    Role: {job_details.job_title}! 
    Job Level: {str(job_details.level_of_job)[10:]}

    """

    job_post += f"""Skills Required: \n"""
    for index, ele in enumerate(job_details.required_skills):
        job_post += f"{job_details.required_skills[index]} \n"
    job_post += f"""

    📩 Interested? Apply now 👉 {job_link}
    
    #Hiring #CareerOpportunity #JoinUs {job_details.hashtag} 🚀
    """
    return job_post