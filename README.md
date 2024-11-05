# Setting Up ngrok with a Flask Application

## Prerequisites

- Python installed on your system
- `pip` package manager
- `virtualenv` (optional but recommended)

## Step 1: Install Flask

First, create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Then, install Flask:

```bash
pip install Flask
```

## Step 2: Create a Simple Flask Application

Create a file named `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(port=5000)
```

Run the Flask application:

```bash
python app.py
```

Your Flask app should now be running on `http://127.0.0.1:5000/`.

## Step 3: Install ngrok

Download and install ngrok from [ngrok's official website](https://ngrok.com/download).

## Step 4: Expose Your Local Flask Server to the Internet

Run ngrok to expose your local Flask server:

```bash
./ngrok http 5000
```

You will see output similar to this:

```
ngrok by @inconshreveable                                                                                                      (Ctrl+C to quit)

Session Status                online
Session Expires               1 hour, 59 minutes
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://abcd1234.ngrok.io -> http://localhost:5000
Forwarding                    https://abcd1234.ngrok.io -> http://localhost:5000
```

Your Flask application is now accessible on the internet via the generated ngrok URL (e.g., `http://abcd1234.ngrok.io`).

## Conclusion

You have successfully set up ngrok with your Flask application. You can now share the ngrok URL to access your Flask app from anywhere.
