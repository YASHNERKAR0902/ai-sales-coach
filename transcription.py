
import os
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version="v1beta")
)


def transcribe_audio(audio_path):

    try:
        print("Uploading audio...")

        audio_file = client.files.upload(file=audio_path)

        print("Detected MIME type:", audio_file.mime_type)
        print("Transcribing audio...")

        interaction = client.interactions.create(
            model="gemini-3.5-transcribe",
            input=[
                {
                    "type": "audio",
                    "uri": audio_file.uri,
                    "mime_type": audio_file.mime_type
                }
            ],
            generation_config={
                "transcription_config": {
                    "mode": {
                        "type": "verbatim",
                        "diarization_mode": "speaker"
                    }
                }
            }
        )

        print("Status:", interaction.status)

        transcript = interaction.output_text or ""

        # Extract speaker annotations
        speaker_segments = []

        for step in interaction.steps or []:
            for content in getattr(step, "content", []) or []:
                for annotation in getattr(content, "annotations", []) or []:

                    if getattr(annotation, "type", None) == "word_info":

                        speaker = annotation.speaker
                        text = annotation.text

                        if speaker and text:
                            speaker_segments.append((speaker, text))

        if not speaker_segments:
            print("No speaker annotations found.")
            return None

        # Map speaker IDs to conversation roles
        speakers = []

        for speaker, text in speaker_segments:
            if speaker not in speakers:
                speakers.append(speaker)

        speaker_mapping = {}

        if len(speakers) >= 1:
            speaker_mapping[speakers[0]] = "Salesperson"

        if len(speakers) >= 2:
            speaker_mapping[speakers[1]] = "Customer"

        # Convert into the format used by our analysis engine
        conversation = []

        for speaker, text in speaker_segments:
            role = speaker_mapping.get(speaker, "Unknown")
            conversation.append((role, text))

        return conversation

    except Exception as e:
        print("ERROR:", repr(e))
        return None
