import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=obj)
    if response.status_code == 200:
        formatted_text = json.loads(response.text)
        emotions = formatted_text['emotionPredictions'][0]['emotion']
        max_score = 0
        dominant_emotion = None
        for k, v in emotions.items():
            if max_score < v:
                max_score = v
                dominant_emotion = k
        r = emotions.copy()
        r['dominant_emotion'] = dominant_emotion
        return r
    elif response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }
    else:
        return {}
