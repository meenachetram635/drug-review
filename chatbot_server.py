from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Root endpoint
@app.route("/")
def home():
    return "Chatbot server is running. Use the /chat endpoint to interact with the chatbot."

# Chatbot endpoint
@app.route("/app", methods=["POST"])
def chat():
    # Get the user input from the request
    data = request.json
    if not data or "query" not in data:
        return jsonify({"error": "Invalid request. 'query' field is required."}), 400

    user_input = data.get("query", "")

    # Simple chatbot logic (replace with your actual logic)
    if "side effect" in user_input.lower():
        response = "Common side effects include nausea, headache, and dizziness."
    elif "dosage" in user_input.lower():
        response = "The recommended dosage is 500mg twice daily."
    else:
        response = f"I'm sorry, I don't understand. You said: {user_input}"

    # Return the response as JSON
    return jsonify({"response": response})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)