from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def detect_emotion(text: str) -> dict:
    """
    Detect emotion from text using VADER Sentiment Analysis.
    Returns a dictionary with emotion type and intensity.
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        emotion = "Positive"
        intensity = compound
    elif compound <= -0.05:
        emotion = "Negative"
        intensity = abs(compound)
    else:
        emotion = "Neutral"
        intensity = 0.5 # Neutral intensity
        
    return {
        "emotion": emotion,
        "intensity": intensity,
        "scores": scores
    }

def get_voice_parameters(emotion_data: dict) -> dict:
    """
    Maps detected emotion to vocal parameters: Rate, Pitch, Volume.
    """
    emotion = emotion_data["emotion"]
    intensity = emotion_data["intensity"]
    
    # Baseline parameters
    params = {
        "rate": 150,    # Default speed
        "pitch": 0,    # Mock pitch offset
        "volume": 0.8,  # Default volume
    }
    
    if emotion == "Positive":
        # Happy: Faster, slightly higher pitch, energetic
        params["rate"] = int(150 + (100 * intensity))
        params["pitch"] = 50 
        params["volume"] = 1.0
    elif emotion == "Negative":
        # Frustrated/Sad: Slower, lower pitch, louder (if frustrated)
        params["rate"] = int(150 - (50 * intensity))
        params["pitch"] = -30
        params["volume"] = 1.1
    else:
        # Neutral: Flat, steady
        params["rate"] = 150
        params["pitch"] = 0
        params["volume"] = 0.8
        
    return params
