
from detoxify import Detoxify

# Load the pre-trained sentiment analysis model
sentiment_model = Detoxify('original')

def perform_sentiment_analysis(text: str) -> float:
    try:
        results = sentiment_model.predict(text)
        print(""*30)
        print(text ,"omar ya zwiiiiin")
        return float(results['toxicity']) 
        
    except Exception as e:
        return -1.0
