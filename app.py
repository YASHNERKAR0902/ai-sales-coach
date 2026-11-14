
import os
import tempfile

from flask import Flask, render_template, request

from analysis import (
    analyze_conversation,
    get_conversation_stats,
    detect_objections
)

from ai_engine import generate_coaching_report
from transcription import transcribe_audio

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Shared analysis function for text and audio

def process_conversation(conversation):

    stats = get_conversation_stats(conversation)
    objections = detect_objections(conversation)
    results = analyze_conversation(conversation)
    report = generate_coaching_report(objections, results)

    total_score = sum(score for category, matched, score in results)
    percentage = round((total_score / 20) * 100, 2)

    # Combine consecutive words from the same speaker
    transcript = []

    for speaker, message in conversation:

        if transcript and transcript[-1][0] == speaker:
            transcript[-1] = (
                speaker,
                transcript[-1][1] + " " + message
            )
        else:
            transcript.append((speaker, message))

    return render_template(
        "results.html",
        stats=stats,
        objections=objections,
        results=results,
        percentage=percentage,
        report=report,
        transcript=transcript
    )



# TEXT ANALYSIS
@app.route("/analyze", methods=["POST"])
def analyze():

    text = request.form.get("conversation", "")

    conversation = []

    for line in text.splitlines():

        if ":" not in line:
            continue

        speaker, message = line.split(":", 1)

        speaker = speaker.strip()
        message = message.strip()

        if speaker in ["Salesperson", "Customer"] and message:
            conversation.append((speaker, message))

    if not conversation:
        return render_template(
            "index.html",
            error="Please enter a valid conversation."
        )

    return process_conversation(conversation)


# AUDIO ANALYSIS
@app.route("/analyze_audio", methods=["POST"])
def analyze_audio():

    audio = request.files.get("audio")

    if not audio or not audio.filename:
        return render_template(
            "index.html",
            error="Please upload an MP3 recording."
        )

    if not audio.filename.lower().endswith(".mp3"):
        return render_template(
            "index.html",
            error="Please upload an MP3 file."
        )

    # Save temporarily for Gemini
    temp_file = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )

    audio_path = temp_file.name
    temp_file.close()

    try:

        audio.save(audio_path)

        # Transcribe and identify speakers
        conversation = transcribe_audio(audio_path)

        if not conversation:
            return render_template(
                "index.html",
                error="Transcription failed. Please try another recording."
            )

        # Analyse using the existing engine
        return process_conversation(conversation)

    except Exception as e:

        print("AUDIO ANALYSIS ERROR:", repr(e))

        return render_template(
            "index.html",
            error="Something went wrong while processing the audio."
        )

    finally:

        if os.path.exists(audio_path):
            os.remove(audio_path)


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
