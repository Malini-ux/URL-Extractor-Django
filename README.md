
# URL Extractor

Fetches URL data scraped from any webpage.

## Overview
A scalable application designed to extract URL data from webpages for analytics. The application leverages caching mechanisms like Redis to improve performance by storing previously extracted data, reducing the need to repeatedly scrape webpages and decreasing response times for users. It allows users to input a webpage URL, extracts all URLs from the specified webpage, and presents them in a user-friendly interface.


![image](https://github.com/Malini-ux/URL-Extractor-Web-app-tool-Django/assets/114894629/7af7d550-fee3-4825-98a7-4c6cb86950f4)

## Features:

**URL Extraction:** Input a webpage URL and utilize BeautifulSoup to extract all URLs contained within the webpage.

**Link Type Detection:** Automatically categorize extracted links as internal, external, relative, or other types.

**Caching Mechanism:** Utilize caching mechanisms like Redis to improve performance.

**User Interface:** Designed with Bootstrap for a responsive and user-friendly interface.

**Debugging Tool:**: Django's built-in debugging tool to measure cache and other performance metrics.




## Dependencies

- Django
- BeautifulSoup
- Redis (optional, for caching mechanism)
- Bootstrap (optional, for user interface)


