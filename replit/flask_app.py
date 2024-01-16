from flask import Flask, render_template, request
import google.generativeai as palm

app = Flask(__name__)


@app.route('/', methods=['GET'])
def generate_text():
  palm.configure(api_key="AIzaSyAWMEx0ByKdMqvuWQSN4uBGNmvfyX88Fw0")

  models = [
      m for m in palm.list_models()
      if 'generateText' in m.supported_generation_methods
  ]
  model = models[0].name

  prompt = request.args.get('question',
                            default="Ask a coding question:",
                            type=str)

  def first_token(prompt):
    tokens = prompt.split(':')
    return tokens[0]

  topic = first_token(prompt)
  prompt = f"""You are an expert at {topic}.  Answer the following coding question briefly,
    yet covering all the important points in it,
    in step by step manner.""" + prompt

  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0.1,
      max_output_tokens=800,
  )

  return render_template('home.html', completion=completion)


if __name__ == "__main__":
  app.run(host="127.0.0.1", debug=True)
