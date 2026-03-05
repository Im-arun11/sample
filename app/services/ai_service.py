from app.services.plagiarism_engine import check_plagiarism

def analyze_code(code: str):

    if not code:
        return {
            "Language": "Unknown",
            "Lines": 0,
            "Import Found": "No",
            "Plagiarism %": 0
        }

    clean_code = code.strip()

    lines = [line for line in clean_code.split("\n") if line.strip() != ""]
    line_count = len(lines)

    import_found = "Yes" if "import" in clean_code else "No"

    if "def " in clean_code or "print(" in clean_code:
        language = "Python"
    elif "#include" in clean_code:
        language = "C"
    else:
        language = "Unknown"

    plagiarism_percent = check_plagiarism(clean_code)

    return {
        "Language": language,
        "Lines": line_count,
        "Import Found": import_found,
        "Plagiarism %": plagiarism_percent
    }