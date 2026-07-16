def split_into_lines(text):

    lines = text.split("\n")

    return [line.strip() for line in lines if line.strip()]

def is_heading(line):

    words = line.split()

    if len(words) <= 4 and not line.endswith("."):
        return True

    return False