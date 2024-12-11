from flask import Flask, request, jsonify, render_template
from langchain.llms import Ollama
import os
from datetime import datetime

app = Flask(__name__)

# Initialize LLM
try:
    llm = Ollama(model="tinyllama")
except Exception as e:
    print(f"Warning: LLM initialization failed: {e}")
    llm = None

# Store chat history
chat_history = []


@app.route("/")
def home():
    """Render the home page"""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat requests"""
    try:
        data = request.json
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400

        if llm is None:
            return jsonify({"error": "LLM not initialized"}), 500

        # Get LLM response
        response = llm(message)

        # Record chat history
        chat_entry = {
            "user_message": message,
            "bot_response": response,
            "timestamp": datetime.now().isoformat(),
        }
        chat_history.append(chat_entry)

        # Remove oldest entries if history gets too long
        if len(chat_history) > 100:
            chat_history.pop(0)

        return jsonify({"response": response, "timestamp": chat_entry["timestamp"]})

    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/history", methods=["GET"])
def get_history():
    """Get chat history"""
    return jsonify(chat_history)


@app.route("/health")
def health():
    """Health check endpoint"""
    status = {
        "status": "healthy",
        "llm_initialized": llm is not None,
        "timestamp": datetime.now().isoformat(),
    }
    return jsonify(status)


def initialize_llm(max_retries=3):
    """Initialize the LLM with retries and model pulling"""
    import subprocess
    import time

    def pull_model():
        try:
            print("Attempting to pull llama2 model...")
            result = subprocess.run(
                ["ollama", "pull", "llama2"], check=True, capture_output=True, text=True
            )
            print(f"Pull output: {result.stdout}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error pulling model: {e}")
            print(f"Error output: {e.stderr}")
            return False
        except FileNotFoundError:
            print("Ollama command not found. Please install Ollama first.")
            return False

    for i in range(max_retries):
        try:
            return Ollama(model="llama2")
        except Exception as e:
            print(f"Attempt {i+1}: LLM initialization failed: {e}")
            if "404" in str(e):  # Model not found error
                print("Attempting to pull the model...")
                if pull_model():
                    print("Model pulled successfully, retrying initialization...")
                    time.sleep(2)  # Wait for model to be ready
                    continue
            time.sleep(2)  # Wait before retry
    return None


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
