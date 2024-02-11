import requests
from django.shortcuts import render
from .forms import URLForm
from .models import Article
from .utils import extract_urls_from_webpage
from django.core.cache import cache

def extract(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            # Check if the data is already cached
            cached_data = cache.get(url)
            if cached_data:
                # If cached data exists, return it directly
                extracted_data = cached_data
           
            else:
   
                response = requests.get(url)
                if response.status_code == 200:
                    html_content = response.text
                    base_url = response.url  # Get the base URL of the webpage
                    extracted_data = extract_urls_from_webpage(html_content, base_url)
                    
                    # Cache the extracted data
                    cache.set(url, extracted_data, timeout=None)  # Set timeout=None for caching indefinitely

                    # Save to database
                    for item in extracted_data:
                        link = item['link']
                        link_type = item['link_type']
                        if not Article.objects.filter(link=link).exists():
                            Article.objects.create(link=link, link_type=link_type)
                else:
                    # Handle invalid response
                    extracted_data = None
    else:
        form = URLForm()
        extracted_data = None
    
    return render(request, "extract_form.html", {"form": form, "extracted_data": extracted_data})
