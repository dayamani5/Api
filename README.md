Real-Time API Integration in Python

This project demonstrates how to consume and work with real-time public APIs using Python. It shows different API use cases such as remote APIs, command-line interaction, API limits, and API usage in a JavaScript Single Page Application (SPA).

Features

Define and understand API interfaces

Fetch data from public APIs using Python

Display API responses in a tabular format

Accept user input from the command line

Demonstrate API rate limiting concepts

Show API usage in JavaScript SPA

Create a live HTML page that fetches API data

APIs Used

Agify API – Predicts age based on name

CoinGecko API – Fetches real-time Bitcoin price

COVID-19 API (disease.sh) – Global COVID statistics

JSONPlaceholder API – Sample API for testing

Technologies Used

Python

Requests library

Tabulate library

Public REST APIs

JavaScript (for SPA demo)

HTML

Project Structure
api-integration/
│
├── api_demo.py
├── spa_api_demo.html   (generated automatically)
└── README.md

Installation and Setup

Clone the repository

git clone <your-repo-url>
cd api-integration


Install required libraries

pip install requests tabulate


Run the program

python api_demo.py

Program Flow

Define API Interface
Displays API endpoint and supported HTTP methods.

Remote API Examples
Fetches and displays data from:

Agify API

CoinGecko API

COVID-19 API

API from Command Line
Takes user input (Post ID) and fetches data from JSONPlaceholder.

API Limits Example
Demonstrates how API rate limits work.

API for JavaScript SPA
Shows sample JavaScript code to fetch API data.

API on Action – SPA Demo
Automatically creates an HTML file that fetches live Bitcoin price using JavaScript.

Output Example

API responses are displayed in table format in the terminal

Bitcoin price is shown live in the browser using JavaScript

Notes

Internet connection is required to access APIs

The spa_api_demo.html file is created automatically

Public APIs used do not require authentication

Learning Outcomes

Understanding REST APIs

Making HTTP requests in Python

Handling API responses and errors

Using APIs in frontend applications

Working with real-time data

Author

Dayamani
B.Tech CSE (AI & ML)
Python API Integration Project
