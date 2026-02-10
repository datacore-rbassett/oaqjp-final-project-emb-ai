from flask import Flask, render_template, redirect, request, url_for
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

def print_comma_list(x):
    if not x:
        s = ""
    elif len(x) == 1:
        s = str(x[0])
    else:
        s = ", ".join(x[:-1])
        s = f"{s} and {x[-1]}"
    return s

@app.route('/emotionDetector')
def emotion_analyzer():
    result = emotion_detector(request.args.get("textToAnalyze"))
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    list = [f"{k}: {v}" for k, v in result.items() if k != 'dominant_emotion']
    output = print_comma_list(list)
    text = f'For the given statement, the system response is {output}.'
    text = text + f'The dominant emtion is <strong>{result["dominant_emotion"]}</strong>.'
    return text