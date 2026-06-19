from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Software Build Automation Tools Project</h1>
    <p>Student: Olcayto Koruk</p>
    <p>This application is deployed using Azure Web App and GitHub Actions.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)