import os
from dotenv import load_dotenv
import openai
load_dotenv()
openai.api_type = os.getenv("OPENAI_API_TYPE")
#openai.api_base = os.getenv("OPENAI_API_BASE")
#openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")
#OPENAI_API_KEY_EMBED="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"

#client = AzureOpenAI(
#  api_key = os.getenv("AZURE_OPENAI_API_KEY"),
#  api_version = "2024-02-01",
##  azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT")
#)

#response = openai.Embedding.create(
    #input = "H",
    #engine= "text-embedding-ada-002"
#)
#print(response)

#print(response.model_dump_json(indent=2))


#Using openai API Directly
import openai

# Initialize the OpenAI API client with your API key
#openai.api_key = "your_openai_api_key_here"

# Define the text for which you want to generate embeddings
text = "This is an example sentence for generating embeddings."

# Generate embeddings using the ADA-002 model
response = openai.Embedding.create(
    model="text-embedding-ada-002",  # Specify the ADA-002 model
    input=text  # Pass the text as a document to generate embeddings
)

# Extract the embeddings from the response
#embeddings = response.data.embeddings

# Print the generated embeddings
print(response)


