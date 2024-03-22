import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyA_j1G7MR9Y6tzE_-l5nc5KHUk1dV9CK6Y"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

def generate_response(query):
    response = model.generate_content(query)
    return response.text

# Example usage
query = input("Enter your query: ")
print(generate_response(query))


