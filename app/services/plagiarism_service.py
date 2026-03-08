def check_plagiarism(code):

    words = code.split()
    unique_words = set(words)

    similarity = 100 - (len(unique_words) / len(words)) * 100 if words else 0

    return f"Estimated similarity: {round(similarity,2)}%"