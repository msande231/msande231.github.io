"""
Starter Code for sending prompt to GPT using OpenAI's API
Author - Nirali Parekh 
"""

import openai
import csv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'
csv_file = 'comma-survey.csv'

# Function to generate GPT-3 prompts based on age and gender
def generate_gpt_prompts(data):
    prompts = []
    for row in data:
        age = row['Age']
        gender = row['Gender']
        # Define the survey prompt - modify it based on the dataset information. 
        # Customize the prompt format as needed, providing the multiple choices to GPT
        prompt = f"""
        You are {age} years old {gender} [...additional demographic information]
        You are invited to participate in a survey. 
        Please answer the following questions:
        1. 
        2. 
        3. 
        4. [...Additional survey questions...]
        """.format(age="AGE_FROM_CSV", gender="GENDER_FROM_CSV")
        prompts.append(prompt)
    return prompts

# Function to poll GPT-3
def poll_gpt3(gpt_prompts, num_responses):
    openai.api_key = api_key
    
    responses = []
    for i in range(num_responses):
        response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose an appropriate engine
        prompt=gpt_prompts[i],
        max_tokens=100,  # Adjust based on the expected response length
        n=1,  # Number of responses to generate
        stop=None,  # You can specify a stopping condition if needed
        )
        responses.append(response.choices[0].text.strip())
    return responses

# Load survey data from csv
survey_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        survey_data.append(row)

# Randomly select 300 rows (you can use a more sophisticated method for randomness). Set seed if needed.
import random
num_responses = 300
selected_data = random.sample(survey_data, num_responses)

# Generate GPT prompts based on the demographics
gpt_prompts = generate_gpt_prompts(selected_data)

# Poll GPT-3 for survey responses (e.g. poll 300 GPT-3 responses)
gpt3_responses = poll_gpt3(gpt_prompts, num_responses)

# Save the responses to a CSV file after processing them as needed
with open('gpt_survey.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Age", "Gender", "Income", "Education", "Location", "Response1", "Response2", ...])  # Add more columns for additional responses
    for response in gpt3_responses:
        writer.writerow(["", "", "", "", "", response, "", ...])  # Fill in demographics as per data
