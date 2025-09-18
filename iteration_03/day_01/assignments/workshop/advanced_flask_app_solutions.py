from flask import Flask, request
import requests

# Creates Simple Flask App
app = Flask(__name__)

# Home Route shows options in HTML using buttons
@app.route("/")
def home():
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Page for Random Info on Cats and Laughs</title>
        </head>
        <body>
            <h1>Welcome to My Flask App</h1>
            <p>
                This is my app about cats and laughs... What would you like do choose?
            </p>
            <a href="/joke"><button>Go to Joke</button></a><br>
            <button id='jokes'>Go to Jokes</button><br>
            <div id="jokes_num_container" style="display:none">
                <form id="joke_form" action="/jokes" method="get">
                    <label for="joke_count">How many jokes would you like to see?:</label>
                    <input type="number" id="joke_count" name="joke_count" required>
                    <button type="submit">Submit</button>
                </form>
            </div>
            <a href="/catfact"><button>Go to Cat Fact</button></a><br>
            <button id='cat_breeds'>Go to Cat Breeds</button><br>
            <div id="cat_breeds_container" style="display:none">
                <form id="cat_breeds_form" action="/catbreeds" method="get">
                    <label for="cat_breeds">How many cat breeds would you like to see?:</label>
                    <input type="number" id="cat_breeds_count" name="cat_breeds_count" required>
                    <button type="submit">Submit</button>
                </form>
            </div>
            <script>
                const joke_button = document.getElementById('jokes');
                const cat_breeds_button = document.getElementById('cat_breeds');
                const joke_inputDiv = document.getElementById('jokes_num_container');
                const cat_breeds_inputDiv = document.getElementById('cat_breeds_container');
                joke_button.addEventListener('click', () => {
                    joke_inputDiv.style.display = 'block';
                });
                cat_breeds_button.addEventListener('click', () => {
                    cat_breeds_inputDiv.style.display = 'block';
                });
            </script>
        </body>
        </html>
"""
    return html_content

# First Route gets random joke
@app.route("/joke")
def joke():
    url = "https://official-joke-api.appspot.com/random_joke" # API for random joke
    response = requests.get(url)
    data = response.json()
    joke = f"{data['setup']} ... {data['punchline']}"
    html_content = f"<h1>Random Joke</h1><p>{joke}</p>"
    return html_content

# Second Route utilizes Query Parameter 'count' with the Random Joke API
@app.route("/jokes")
def jokes():
    count = int(request.args.get("joke_count", 1))
    jokes = []
    for _ in range(count):
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        jokes.append(f"{data['setup']} ... {data['punchline']}")
    joke_html = "<br><br>".join(jokes)
    html_content = f"<h1>Here are {count} joke(s):</h1><p>{joke_html}</p>"
    return html_content

# Third Route utilizes GET method with Cat Fact API
@app.route("/catfact")
def cat_fact():
    url = "https://catfact.ninja/fact" # API for cat fact
    response = requests.get(url)
    data = response.json()
    html_content = (f"""
        <h1>Cat Fact</h1>
        <p>Random Cat Fact: {data['fact']}</p>
        """)
    return html_content

# Fourth Route utilizes Query Parameter 'limit' with Cat Breeds API
@app.route("/catbreeds")
def cat_breeds():
    limit = int(request.args.get("cat_breeds_count", 1))
    url = f"https://catfact.ninja/breeds?limit={limit}" # API for cat fact
    response = requests.get(url)
    response = response.json()
    breeds_list = []
    for breed in response['data']:
        breeds_list.append(f"Breed: {breed['breed']} Country: {breed['country']}")
    html_content = (f"""
        <h1>Cat Breeds</h1>
        <p>{"<br></br>".join(breeds_list)}</p>
    """)
    return html_content

if __name__ == "__main__":
    app.run()