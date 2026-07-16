const resumeInput = document.getElementById("resume");
const jobDescription = document.getElementById("job-description");
const analyzeButton = document.getElementById("analyze-btn");
const fileName = document.getElementById("file-name");
const resultContent = document.getElementById("result-content");

// Display selected file name
resumeInput.addEventListener("change", function () {

    if (resumeInput.files.length > 0) {
        fileName.textContent = resumeInput.files[0].name;
    } else {
        fileName.textContent = "No file selected";
    }

});

// Analyze button click
analyzeButton.addEventListener("click", function () {

    const resume = resumeInput.files[0];
    const jd = jobDescription.value.trim();

    if (!resume) {
        alert("Please select a resume.");
        return;
    }

    if (jd === "") {
        alert("Please paste the job description.");
        return;
    }

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jd);

    // Loading Message
    resultContent.innerHTML = `
        <h3>Analyzing Resume...</h3>
        <p>Please wait while we analyze your resume.</p>
    `;

    fetch("http://127.0.0.1:8000/analyze", {

        method: "POST",
        body: formData

    })
    .then(response => response.json())

    .then(data => {

        resultContent.innerHTML = `

        <p><strong>Resume:</strong> ${data.filename}</p>

        <div class="score-card">
            <h2>🎯 Keyword ATS Score</h2>
            <h1>${data.ats_score}%</h1>
        </div>

        <br>

        <div class="score-card">
            <h2>🤖 Weighted AI Semantic Score</h2>
            <h1>${data.semantic_score}%</h1>
        </div>

        <br>

        <h2>📊 Section-wise AI Scores</h2>

        <table class="section-table">
            <tr>
                <th>Resume Section</th>
                <th>Similarity</th>
            </tr>

            <tr>
                <td>💻 Skills</td>
                <td>${data.section_scores.skills.toFixed(2)}%</td>
            </tr>

            <tr>
                <td>📁 Projects</td>
                <td>${data.section_scores.projects.toFixed(2)}%</td>
            </tr>

            <tr>
                <td>🎓 Education</td>
                <td>${data.section_scores.education.toFixed(2)}%</td>
            </tr>

            <tr>
                <td>💼 Experience</td>
                <td>
                    ${
                        data.section_scores.experience > 0
                        ? data.section_scores.experience.toFixed(2) + "%"
                        : "Not Available"
                    }
                </td>
            </tr>

        </table>

        <br>

        <h3>✅ Matched Skills</h3>
        <ul>
            ${data.matched_skills.map(skill => `<li>${skill}</li>`).join("")}
        </ul>

        <h3>❌ Missing Skills</h3>
        <ul>
            ${data.missing_skills.map(skill => `<li>${skill}</li>`).join("")}
        </ul>

        <h3>💡 Suggestions</h3>
        <ul>
            ${data.suggestions.map(suggestion => `<li>${suggestion}</li>`).join("")}
        </ul>

        <hr>

        <h2>🤖 AI Resume Review</h2>

        <h3>💪 Strengths</h3>
        <ul>
            ${data.feedback.strengths.map(item => `<li>${item}</li>`).join("")}
        </ul>

        <h3>⚠ Weaknesses</h3>
        <ul>
            ${data.feedback.weaknesses.map(item => `<li>${item}</li>`).join("")}
        </ul>

        <h3>🚀 Recommendations</h3>
        <ul>
            ${data.feedback.recommendations.map(item => `<li>${item}</li>`).join("")}
        </ul>

    `;

    })

    .catch(error => {

        console.error(error);

        resultContent.innerHTML = `
            <h2>❌ Error</h2>
            <p>Something went wrong while analyzing your resume.</p>
        `;

    });

});