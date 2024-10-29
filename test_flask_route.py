from flask import Flask, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    if request.is_json:
        data = request.get_json()
        
        # Extract query information and process based on the LLM instruction
        query = data.get('query')
        
        # Check if "search" is part of the query to determine the task
        if query and query.startswith("search "):
            search_terms = query[len("search "):]  # Extract terms after "search"
            
            # Here, we simulate an API request with these terms
            # For example, you might call an external API using `requests`
            # response_data = requests.get(f"https://api.example.com/search?query={search_terms}").json()
            
            # Mocked response for demonstration
            response_data = {
                "search_results": f"Results for '{search_terms}'",  # Placeholder for actual API response
                "status": "success"
            }

            # Log the API response
            logging.info(f"API Response: {response_data}")

            return jsonify(response_data), 200
        else:
            # Respond normally if no "search" instruction is found
            response = {
                "response": f"Normal response based on knowledge for: '{query}'",
                "status": "success"
            }

            # Log the normal response
            logging.info(f"Response: {response}")

            return jsonify(response), 200

    else:
        return jsonify({"error": "Invalid input. Expected JSON data."}), 400

if __name__ == '__main__':
    app.run(debug=True)
