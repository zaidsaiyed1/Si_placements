from bs4 import BeautifulSoup
import requests
from utils.formatter import normalize_job

def scrape_internshala_jobs(description, location,exprience_level):
    description1 = description.strip().lower()
    experience_level = exprience_level.strip().lower()
    url = ''
    if experience_level=="fresher":
        url = f"https://internshala.com/fresher-jobs/{description}-jobs-in-{location}/"
    else:
        url = f"https://internshala.com/jobs/{description}-jobs-in-{location}/experience-{exprience_level}/"
    
    
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify())
    jobs = []
    for job_card in soup.find_all('div', class_='internship_meta experience_meta'):
#           print(job_card)        
          title = job_card.find('a', class_='job-title-href').text.strip()
          company = job_card.find('p', class_='company-name').text.strip()
          locations = job_card.find('p',class_='locations').text.strip()
          salary = job_card.find('span',class_='desktop').text.strip()
          experience_tag = job_card.find('i', class_='ic-16-briefcase')
          exprience_required = experience_tag.find_next('span').text.strip()
          job_portol = "Internshala"
          job_url = "https://internshala.com"+job_card.find('a', class_='job-title-href')['href']
          if description1 in title.lower():
              jobs.append(normalize_job({
              'title': title,
              'company': company,
              'locations': locations,
              'salary': salary,
              'exprience_required': exprience_required,
              'job_portol': job_portol,
              'job_url': job_url
               }))
          
          
    return jobs