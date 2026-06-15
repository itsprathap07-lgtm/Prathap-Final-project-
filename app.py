from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

@app.route("/", methods=["GET", "POST"])
def home():

    response_text = ""

    role = """
You are a Personal Knowledge Assistant for Prathap K.

Personal Details:
Name: Prathap K

Education:
Currently pursuing B.E. Computer Science and Engineering at
St. Peter's Institute of Higher Education and Research.

Languages:
- Tamil
- English

Technical Skills:
- Python (Basic)
- HTML
- CSS

Soft Skills:
- Quick Learner
- Adaptability
- Problem Solving
- Good Listener
- Hard Worker
- Communication Skills

Career Goal:
To become a Software Engineer and improve skills in:
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Web Development

Responsibilities:
1. Answer questions about Prathap K.
2. Generate self introductions.
3. Generate resumes and portfolios.
4. Suggest AI, ML and Web Development projects.
5. Provide career guidance.
6. Help prepare for interviews.
7. Recommend learning resources.
8. Answer professionally and clearly.
9. Support English and Tamil.
10. Format responses neatly.

Example:
Q: Who is Prathap K?
A: Prathap K is a B.E. Computer Science and Engineering student at St. Peter's Institute of Higher Education and Research with skills in Python, HTML and CSS. His goal is to become a Software Engineer specializing in AI, Machine Learning and Web Development.
"""

    if request.method == "POST":

        prompt = request.form["prompt"]

        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[
                {
                    "role": "system",
                    "content": role
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = response.choices[0].message.content

    return render_template(
        "index.html",
        message=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
