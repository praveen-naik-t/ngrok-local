from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhooks/reservations', methods=['POST'], )
def receive_stripe_webhook():
    """Receives a webhook payload from Stripe.
    """

    # Try to parse a webhook payload, get upset if we couldn't
    # parse any JSON in the body:
    print("recieved webhook", request)
    if request.is_json:
        stripe_payload = request.json
    else:
        stripe_payload = request.form.to_dict()

    print("printing response", stripe_payload)
    if not stripe_payload:
        return jsonify(message="Could not parse webhook payload"), 400
    
    response_data = {
        "instruction":"redirect",
        "url": {'name': 'https://www.google.com'},
    }
    print("returning response")
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(debug=True)