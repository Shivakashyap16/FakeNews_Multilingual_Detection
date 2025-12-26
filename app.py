from flask import Flask, render_template, request
from src.predict import predict_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    language = ""
    news_text = ""

    if request.method == "POST":
        if "analyze" in request.form:
            news_text = request.form["news"]
            result, language = predict_news(news_text)
        elif "clear" in request.form:
            news_text = ""
            result = ""
            language = ""

    return render_template(
        "index.html",
        result=result,
        language=language,
        news_text=news_text
    )

if __name__ == "__main__":
    app.run(debug=True)
