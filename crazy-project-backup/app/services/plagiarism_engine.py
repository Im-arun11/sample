from difflib import SequenceMatcher

sample_code = """
def add(a, b):
    return a + b
"""

def normalize_code(code):
    return code.replace(" ", "").replace("\n", "").lower()

def calculate_similarity(code1, code2):
    return SequenceMatcher(None, code1, code2).ratio()

def check_plagiarism(user_code):
    user_code = normalize_code(user_code)
    ref_code = normalize_code(sample_code)
    similarity = calculate_similarity(user_code, ref_code)
    return round(similarity * 100, 2)