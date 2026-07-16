import re


SECTION_HEADERS = {
    "skills": [
        "skills",
        "technical skills",
        "technical expertise",
        "technologies"
    ],

    "projects": [
        "projects",
        "personal projects",
        "academic projects"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment"
    ],

    "education": [
        "education",
        "academic details",
        "academic background"
    ]
}


def extract_sections(text):

    sections = {
        "skills": "",
        "projects": "",
        "experience": "",
        "education": ""
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

            if lower in headers:

                current_section = section
                found = True
                break

        if found:
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections