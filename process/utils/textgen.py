import os
import openai
import random


#TextGen utilizes Open AI GPT-3 to generate a respones when given a prompt
class TextGen():
  def __init__(self):
    self.prompts = [    
      "Give the cat a a random name that sounds funny and make it all lowercase followed by'?'",
      "Make a cat and say something funny about it",
      "say something weird",
      "make a weird sound and verbalize it",
      "make a cute cat noise",
      "give me a fun fact about cats"
    ]
    
    self.key = "sk-<YOUR OPENAI API KEY>"
  
  def get_textdata(self):
    openai.api_key = self.key
    response = openai.Completion.create(
      engine="text-davinci-001",
      prompt=random.choice(self.prompts),
      temperature=1.0,
      max_tokens=100,
    )
    return response['choices'][0]['text']





