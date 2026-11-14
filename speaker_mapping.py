
def map_speakers(transcript, salesperson_label):

    conversation = []

    if salesperson_label not in ["Speaker 1", "Speaker 2"]:
        raise ValueError("Invalid salesperson speaker.")

    for line in transcript.splitlines():

        if ":" not in line:
            continue

        speaker, message = line.split(":", 1)

        speaker = speaker.strip()
        message = message.strip()

        if speaker == salesperson_label:
            role = "Salesperson"

        elif speaker in ["Speaker 1", "Speaker 2"]:
            role = "Customer"

        else:
            continue

        if message:
            conversation.append((role, message))

    return conversation
