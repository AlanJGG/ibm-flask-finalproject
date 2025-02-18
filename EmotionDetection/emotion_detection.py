import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=myobj, headers=headers)
        if response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response_data = json.loads(response.text)
        emotion_scores = response_data['emotionPredictions'][0]['emotion']
        anger_score = emotion_scores.get('anger', 0)
        disgust_score = emotion_scores.get('disgust', 0)
        fear_score = emotion_scores.get('fear', 0)
        joy_score = emotion_scores.get('joy', 0)
        sadness_score = emotion_scores.get('sadness', 0)

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    except Exception:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
