import requests
import json

def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response =requests.post(url, headers = headers , json= input_json)
    
    if response.status_code == 200:
        data= response.json()

        if "emotionPredictions" in data and isinstance(data["emotionPredictions"], list):
            emotions = data["emotionPredictions"][0].get("emotion", {})
            filtered_emotions = {key: emotions[key] for key in ["anger", "disgust", "fear", "joy", "sadness"] if key in emotions}
            return filtered_emotions
        else:
            return {"error":"response failed"}
    else:
        return {"error":"request failed"}

