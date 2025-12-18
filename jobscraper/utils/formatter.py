
def clean_text(text):
    return text.replace("\n", " ").strip() if text else None

def format_salary(salary):
    if not salary:
        return None
    return clean_text(salary)

def format_experience(exp):
    if exp is None:
        return "Not specified"

    exp = clean_text(exp)

    if not exp:
        return "Not specified"

    if "fresher" in exp.lower():
        return "Fresher"

    return exp



def normalize_job(job):
    return {
        "title": clean_text(job.get("title")),
        "company": clean_text(job.get("company")),
        "location": clean_text(job.get("locations")),
        "salary": format_salary(job.get("salary")),
        "experience": format_experience(job.get("exprience_required")),
        "portal": job.get("job_portol"),
        "url": job.get("job_url"),
    }
