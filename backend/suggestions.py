def generate_suggestions(missing_skills):

    suggestion_map = {
        "Docker": "Learn Docker and mention a Dockerized project in your resume.",
        "Linux": "Highlight your Linux command-line experience if you have used Ubuntu or WSL.",
        "Git": "Use Git regularly and include your GitHub profile in your resume.",
        "FastAPI": "Build a REST API project using FastAPI and showcase it in your projects section.",
        "Python": "Strengthen your Python skills by solving problems and building backend applications.",
        "SQL": "Practice SQL queries and mention database projects using MySQL or PostgreSQL.",
        "React": "Develop a React project and include it in your portfolio.",
        "Machine Learning": "Complete a machine learning project using scikit-learn or TensorFlow.",
        "Deep Learning": "Build a neural network project and explain the technologies used.",
        "Computer Networks": "Revise networking concepts and mention networking-related coursework if relevant."
    }

    suggestions = []

    for skill in missing_skills:

        if skill in suggestion_map:
            suggestions.append(suggestion_map[skill])
        else:
            suggestions.append(f"Consider adding or learning {skill}.")

    return suggestions