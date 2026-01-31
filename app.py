from utils.genai_utils import generate_text
from utils.audio_utils import text_to_audio
from utils.image_utils import generate_image_prompt
from utils.code_utils import code_prompt
from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Define and create the audio directory
AUDIO_FOLDER = "outputs/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    topic = data.get("topic")
    mode = data.get("mode")
    level = data.get("level", "beginner")

    if not topic or not mode:
        return jsonify({"error": "Missing topic or mode"}), 400

    # Handle Text Mode
    if mode == "text":
        prompt = f"Explain {topic} in the context of Machine Learning. Use Markdown, include a definition, intuition, and a real-world example."
        content = generate_text(prompt) 
        return jsonify({"result": content})

    # Handle Code Mode
    if mode == "code":
        prompt = code_prompt(topic, level)
        code = generate_text(prompt)
        return jsonify({"result": code})

    # Handle Audio Mode
    if mode == "audio":
        script = generate_text(topic, mode, level)
        audio_path = text_to_audio(script)
        filename = os.path.basename(audio_path)
        return jsonify({"audio": f"/audio/{filename}"})

    # Handle Image/Diagram Prompt Mode
    if mode == "image":
        prompt = generate_image_prompt(topic)
        # Using the utility to generate a text description for the diagram
        result = generate_text(topic, mode) 
        return jsonify({"result": result, "prompt": prompt})

    return jsonify({"error": "Invalid mode"}), 400

@app.route("/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(
        directory=AUDIO_FOLDER,
        path=filename,
        as_attachment=False
    )

if __name__ == "__main__":
    app.run(debug=True)