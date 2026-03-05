from difflib import SequenceMatcher

def check_plagiarism(code):

    # Example comparison (in real system compare with database)
    sample_code = """
def add(a,b):
    return a+b
"""

    similarity = SequenceMatcher(None, code, sample_code).ratio()

    percentage = round(similarity * 100, 2)

    return percentage