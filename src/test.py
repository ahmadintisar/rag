#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_type = os.getenv("OPENAI_API_TYPE")
#openai.api_base = os.getenv("OPENAI_API_BASE")
#openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")


#response = openai.ChatCompletion.create(
  #engine="xraise-35turbo", # replace this value with the deployment name you chose when you deployed the associated model.
  #messages = [{"role":"system","content":"What is an api?"},{"role":"user","content":"How much is a PS5?"},{"role":"assistant","content":"I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"},{"role":"user","content":"I am interested in buying an Xbox?"},{"role":"assistant","content":"Great! There are several Xbox models available in the market, including the Xbox Series X, Xbox Series S, and Xbox One. The Xbox Series X is the latest and most powerful console, while the Xbox Series S is a more affordable option that still offers great performance. The Xbox One is the previous generation console, but it still has a large library of games available to play.\n\nBefore purchasing an Xbox, you may want to consider factors such as your budget, the types of games you want to play, and whether you want to play games in 4K resolution. Once you have decided on a console, you can purchase it from a retailer or directly from the Xbox website. Let me know if you have any other questions or concerns!"},{"role":"user","content":"Which models are 4K?"},{"role":"assistant","content":"Both the Xbox Series X and Xbox One X support 4K resolution gaming. The Xbox Series S, on the other hand, supports up to 1440p resolution gaming, but it can upscale games to 4K. It's worth noting that in order to take advantage of 4K gaming, you'll need a 4K TV or monitor that supports HDR (High Dynamic Range) and HDMI 2.0 or higher."}],
  #temperature=0.3,
  #max_tokens=350,
  #top_p=0.95,
  #frequency_penalty=0,
  #presence_penalty=0,
  #stop=None)

#print(response)

#response = openai.ChatCompletion.create(
  #engine="gpt-3.5turbo", # replace this value with the deployment name you chose when you deployed the associated model.
  #messages = [{"role":"system","content":"What is an api?"},{"role":"user","content":"How much is a PS5?"},{"role":"assistant","content":"I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"},{"role":"user","content":"I am interested in buying an Xbox?"},{"role":"assistant","content":"Great! There are several Xbox models available in the market, including the Xbox Series X, Xbox Series S, and Xbox One. The Xbox Series X is the latest and most powerful console, while the Xbox Series S is a more affordable option that still offers great performance. The Xbox One is the previous generation console, but it still has a large library of games available to play.\n\nBefore purchasing an Xbox, you may want to consider factors such as your budget, the types of games you want to play, and whether you want to play games in 4K resolution. Once you have decided on a console, you can purchase it from a retailer or directly from the Xbox website. Let me know if you have any other questions or concerns!"},{"role":"user","content":"Which models are 4K?"},{"role":"assistant","content":"Both the Xbox Series X and Xbox One X support 4K resolution gaming. The Xbox Series S, on the other hand, supports up to 1440p resolution gaming, but it can upscale games to 4K. It's worth noting that in order to take advantage of 4K gaming, you'll need a 4K TV or monitor that supports HDR (High Dynamic Range) and HDMI 2.0 or higher."}],
  #temperature=0.3,
  #max_tokens=350,
  #top_p=0.95,
  #frequency_penalty=0,
  #presence_penalty=0,
  #stop=None)

#print(response)

import openai

# Initialize the OpenAI API client with your API key
#openai.api_key = "your_openai_api_key_here"

import openai

# Initialize the OpenAI API client with your API key
openai.api_key = "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"

# Create a list of messages representing the conversation history
messages = [
    {"role": "system", "content": "What is an API?"},
    {"role": "user", "content": "How much is a PS5?"},
    {"role": "assistant", "content": "I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"},
    {"role": "user", "content": "I am interested in buying an Xbox?"},
    {"role": "assistant", "content": "Great! There are several Xbox models available in the market, including the Xbox Series X, Xbox Series S, and Xbox One. The Xbox Series X is the latest and most powerful console, while the Xbox Series S is a more affordable option that still offers great performance. The Xbox One is the previous generation console, but it still has a large library of games available to play.\n\nBefore purchasing an Xbox, you may want to consider factors such as your budget, the types of games you want to play, and whether you want to play games in 4K resolution. Once you have decided on a console, you can purchase it from a retailer or directly from the Xbox website. Let me know if you have any other questions or concerns!"},
    {"role": "user", "content": "Which models are 4K?"},
    {"role": "assistant", "content": "Both the Xbox Series X and Xbox One X support 4K resolution gaming. The Xbox Series S, on the other hand, supports up to 1440p resolution gaming, but it can upscale games to 4K. It's worth noting that in order to take advantage of 4K gaming, you'll need a 4K TV or monitor that supports HDR (High Dynamic Range) and HDMI 2.0 or higher."}
]

# Make a chat completion request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Specify the model you want to use
    messages=messages
)

# Print the generated response
print(response.choices[0].message.content)


