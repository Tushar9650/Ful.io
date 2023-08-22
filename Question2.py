import requests
from bs4 import BeautifulSoup
import re

# Function to extract social links, email, and contact details from a website
def extract_details(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract social links
            social_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if re.search(r'facebook\.com', href, re.I):
                    social_links.append(href)
                elif re.search(r'linkedin\.com', href, re.I):
                    social_links.append(href)
            
            # Extract email address
            email = None
            for paragraph in soup.find_all('p'):
                if re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', paragraph.get_text()):
                    email = paragraph.get_text()
                    break
            
            # Extract contact details (phone number)
            contact = None
            for paragraph in soup.find_all('p'):
                if re.search(r'\+?\d{1,4}[\s-]?\d{1,15}', paragraph.get_text()):
                    contact = paragraph.get_text()
                    break
            
            # Print the extracted details
            print("Social links -")
            for link in social_links:
                print(link)
            if email:
                print("Email/" + email)
            if contact:
                print("Contact:\n" + contact)
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
    
    except Exception as e:
        print("An error occurred:", str(e))

# User input for the website URL
url = input("Enter the website URL: ")

# Call the function to extract details
extract_details(url)
