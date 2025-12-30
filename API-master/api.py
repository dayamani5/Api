import requests
from tabulate import tabulate

# Step 1: Defining API Interface
def define_api_interface():
    print("\n-- Defining API Interface --")
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    supported_methods = ["GET"]
    print(f"API Endpoint: {api_url}")
    print(f"Supported Methods: {supported_methods}")

# Step 2: Remote API Examples
def remote_api_example():
    print("\n-- Remote API Examples --")

    # Agify API
    url_age = "http://api.agify.io?name=michael"
    try:
        response = requests.get(url_age)
        response.raise_for_status()
        data = response.json()
        print("\nAgify API Response (Predicted Age):")
        print(tabulate(data.items(), headers=["Field", "Value"]))
    except requests.exceptions.RequestException as e:
        print("Error fetching Agify API:", e)

    # Coingecko API
    url_crypto = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?vs_currencies=usd&ids=bitcoin"
    )
    try:
        response = requests.get(url_crypto)
        response.raise_for_status()
        crypto_data = response.json()
        print("\nCoingecko API Response (Bitcoin Price USD):")
        print(tabulate(crypto_data["bitcoin"].items(), headers=["Currency", "Price"]))
    except requests.exceptions.RequestException as e:
        print("Error fetching Coingecko API:", e)

    # COVID-19 API
    url_covid = "https://disease.sh/v3/covid-19/all"
    try:
        response = requests.get(url_covid)
        response.raise_for_status()
        covid_data = response.json()
        print(
            f"\nCOVID-19 Global Cases: {covid_data['cases']:,}, "
            f"Deaths: {covid_data['deaths']:,}"
        )
    except requests.exceptions.RequestException as e:
        print("Error fetching COVID-19 API:", e)

# Step 3: API from Command Line
def api_from_command_line():
    print("\n-- API From Command Line Example --")
    try:
        post_id = int(input("Enter a post ID (1-100): "))
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        response.raise_for_status()
        post = response.json()
        print("\nPost Details:")
        print(tabulate(post.items(), headers=["Field", "Value"]))
    except ValueError:
        print("Invalid input. Please enter a numeric post ID.")
    except requests.exceptions.RequestException as e:
        print("Error fetching post:", e)

# Step 4: API Limits Example
def api_limits_example():
    print("\n-- API Limits Example --")
    max_requests_per_minute = 5
    current_requests = 3
    print(f"Max requests allowed per minute: {max_requests_per_minute}")
    if current_requests < max_requests_per_minute:
        print("You can make more requests.")
    else:
        print("Request limit reached. Please wait.")

# Step 5: API for JavaScript SPA (Example Code)
def api_for_js_spa():
    print("\n-- API in JavaScript SPA --")
    example_js_code = """
fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
  .then(response => response.json())
  .then(data => console.log(data.bitcoin.usd))
  .catch(error => console.error(error));
"""
    print("Example JS code:\n", example_js_code)

# Step 6: API on Action – JavaScript SPA Demo
def api_on_action_js_spa():
    print("\n-- API on Action: JavaScript SPA Demo --")

    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>SPA API Demo</title>
</head>
<body>
    <h2>Bitcoin Price in USD</h2>
    <div id="price">Loading...</div>

    <script>
        fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
            .then(response => response.json())
            .then(data => {
                document.getElementById('price').innerText =
                    'Bitcoin Price USD: ' + data.bitcoin.usd;
            })
            .catch(error => {
                document.getElementById('price').innerText =
                    'Error fetching data';
                console.error(error);
            });
    </script>
</body>
</html>
"""

    file_name = "spa_api_demo.html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"SPA demo HTML file created: {file_name}")
    print("Open it in a browser to see live API data.")

# ================= MAIN PROGRAM =================
if __name__ == "__main__":
    print("\n==== ENHANCED REAL-TIME API INTEGRATION IN PYTHON DEMO ====")

    define_api_interface()
    remote_api_example()
    api_from_command_line()
    api_limits_example()
    api_for_js_spa()
    api_on_action_js_spa()

    print("\n==== DEMO COMPLETED ====")
