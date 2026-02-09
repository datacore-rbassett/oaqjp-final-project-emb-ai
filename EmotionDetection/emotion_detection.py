import requests
import json

def emotion_detector(text_to_analyze):
    ''' analyze emotion/sentiment of given text, 
        return metrics in a dictionary
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=obj)
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