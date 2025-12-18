from django.shortcuts import render,redirect
from scraper.internshala_scraper import scrape_internshala_jobs
import json
import os
from django.conf import settings

# Create your views here.
def home(request):
              context = {}
              return render(request, 'search.html',context)

OUTPUT_PATH = os.path.join(
    settings.BASE_DIR,
    "outputs",
    "json.json"
)

def save_jobs_to_json(jobs):
        if not os.path.exists(OUTPUT_PATH) or os.stat(OUTPUT_PATH).st_size == 0:
         with open(OUTPUT_PATH, 'w', encoding="utf-8") as file:
             json.dump([], file,ensure_ascii=False)
               
        with open(OUTPUT_PATH, 'r', encoding="utf-8") as f:
   
            data_list = json.load(f)
     
        data_list.append(jobs)

        with open(OUTPUT_PATH, 'w', encoding="utf-8") as f:

            json.dump(data_list, f, indent=4,ensure_ascii=False)

def search_jobs(request):
    if request.method == 'POST':
              description = request.POST['description']
              location = request.POST['location']
              experience_level = request.POST['experience_level']
              jobs_internshala=scrape_internshala_jobs(description, location, experience_level)
              save_jobs_to_json(jobs_internshala)    
#     print(jobs)
    return redirect('/')