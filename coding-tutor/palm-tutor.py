import google.generativeai as palm

palm.configure(api_key='AIzaSyAWMEx0ByKdMqvuWQSN4uBGNmvfyX88Fw0')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

prompt = input("Ask a coding question:")

def first_token(prompt):
  tokens = prompt.split(':')
  return tokens[0]

topic = first_token(prompt)
prompt = f"""You are an expert at {topic}.  Answer the following coding question briefly,
  yet covering all the important points in it,
 in step by step manner.""" + prompt

completion = palm.generate_text(
    model = model,
    prompt = prompt,
    temperature = 0.1,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)