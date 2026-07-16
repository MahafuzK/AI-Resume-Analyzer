SECTION_HEADERS = {

    "skills": [
        "required skills",
        "requirements",
        "skills",
        "technical skills"
    ],

    "responsibilities": [
        "responsibilities",
        "job responsibilities",
        "duties",
        "what you'll do"
    ],

    "qualification": [
        "qualification",
        "qualifications",
        "education",
        "eligibility"
    ]

}


def extract_jd_sections(text):

    sections = {
        "skills": "",
        "responsibilities": "",
        "qualification": ""
    }

    current_section = None

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        lower = line.lower()

        found = False

        for section, headers in SECTION_HEADERS.items():

            # Match headings like:
            # Responsibilities
            # Responsibilities:
            # Required Skills:
            # Qualifications:
            if any(lower.startswith(header) for header in headers):

                current_section = section
                found = True
                break

        if found:
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections