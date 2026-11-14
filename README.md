# AI Sales Coach 🤖

**An AI-powered sales conversation analysis and coaching platform.**

AI Sales Coach transforms recorded sales conversations into structured performance insights, helping salespeople understand their strengths, identify customer objections, and improve their communication.

## 🎯 Problem Statement

Sales conversations contain valuable information about customer needs, objections, and salesperson performance. However, manually reviewing every conversation can be time-consuming and inconsistent.

Sales teams need a simpler way to analyse conversations and identify areas for improvement.

## 💡 Our Solution

AI Sales Coach analyses sales conversations using audio transcription and automated analysis techniques. It provides performance scores, identifies customer objections, and generates actionable coaching recommendations.

## ✨ Key Features

- **Audio Transcription:** Converts uploaded MP3 sales recordings into text using Google's Gemini API.
- **Speaker Identification:** Uses speaker diarisation to distinguish between participants in a conversation.
- **Conversation Analysis:** Analyses the conversation to evaluate salesperson performance.
- **Performance Scoring:** Generates scores across four categories:
  - Customer Discovery
  - Communication
  - Objection Handling
  - Follow-up and Closing
- **Objection Detection:** Identifies common customer objections relating to price, timing, trust, need, and authority.
- **AI Coaching Report:** Provides strengths, weaknesses, and recommendations for improvement.
- **Transcript Display:** Displays the transcribed conversation alongside its analysis.

## ⚙️ How It Works

1. The user uploads an MP3 recording or enters a conversation manually.
2. Gemini processes the audio and generates a transcript with speaker information.
3. The conversation is passed to the Python analysis engine.
4. The system identifies objections and evaluates salesperson performance.
5. A coaching report is generated and displayed through the web interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic and analysis |
| Flask | Web application framework |
| Google Gemini API | Audio transcription and speaker diarisation |
| HTML | Webpage structure |
| CSS | User interface and styling |
| Git & GitHub | Version control and project hosting |

## 🖥️ Project Structure

```text
AI-Sales-Coach/
│
├── app.py
├── ai_engine.py
├── analysis.py
├── scoring.py
├── transcription.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Sales-Coach.git
```

### 2. Navigate to the project directory

```bash
cd AI-Sales-Coach
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Set your Gemini API key as an environment variable.

On Windows CMD:

```cmd
set GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own API key. Never share or commit your API key.

### 5. Run the application

```bash
py app.py
```

### 6. Open the website

Visit:

```text
http://127.0.0.1:5000
```

## 🔬 Current Limitations

- Performance scoring currently uses rule-based keyword matching.
- Speaker roles are assigned based on the order in which speakers are detected, which may not always be accurate.
- Analysis depends on the quality of the audio transcription.
- The application currently supports MP3 audio uploads.

## 🔮 Future Scope

- Context-aware AI conversation analysis.
- Improved salesperson and customer role identification.
- Multilingual conversation analysis.
- Manager dashboards for analysing multiple sales calls.
- CRM integration.
- More detailed performance trends and insights.

## 🌟 Expected Impact

AI Sales Coach aims to make sales performance analysis more accessible and efficient by turning conversations into meaningful feedback.

It helps salespeople recognise improvement opportunities and supports more informed, consistent coaching.

---

**Built as a hackathon project.**

