import openai
openai.api_key = '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'
promt = input('Enter your command')
response = openai.Completion.create(
  model="davinci",
  prompt=promt,
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
text = response.get('choices')[0].get('text')
print(text)