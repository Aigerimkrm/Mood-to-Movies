from transformers import pipeline

# Load once
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def get_emotion_scores(sentences, candidate_labels):
    if isinstance(sentences, str):
        sentences = [sentences]

    results = classifier(sentences, candidate_labels=candidate_labels)
    if isinstance(results, dict):
        results = [results]
    
    return [dict(zip(r['labels'], r['scores'])) for r in results]
