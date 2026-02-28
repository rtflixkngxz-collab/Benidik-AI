from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"  # ضع مفتاحك هنا

@app.route("/api", methods=["POST"])
def api():
    data = request.json
    user_msg = data.get("message","")

    # رد افتراضي من ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":user_msg}]
    )
    reply = response['choices'][0]['message']['content']

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)