from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from src.query_llm import process_input  # Your function to process LLM input
from src.governance_chatbot.ai.ai_router import query_llm
import logging
import asyncio
import json

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.websocket("/ws/llm_response")
async def llm_response(websocket: WebSocket):
    await websocket.accept()
    logging.info("WebSocket connection established.")

    try:
        while True:
            query = await websocket.receive_text()  # Receive query from Speech Recognition Project
            logging.info(f"Received query: {query}")

            try:
                # Process the input using the LLM (asynchronously)
                llm_response = await asyncio.to_thread(query_llm, query)

                # Prepare response to send
                response_to_send = prepare_response(llm_response)

                # Log the response that will be sent back to the client
                logging.info(f"Sending response: {response_to_send}")

                # Stream the LLM response back to the Speech Recognition Project
                await websocket.send_text(response_to_send)

            except Exception as e:
                logging.error(f"Error processing input: {e}")
                await websocket.send_text("An error occurred while processing your request.")

    except WebSocketDisconnect:
        logging.info("LLM response WebSocket disconnected.")

def prepare_response(response):
    """Prepare the response based on the LLM output."""
    if response is None:
        logging.warning("LLM response is None, sending default message.")
        return "No response generated."
    
    if isinstance(response, str):
        return response
    elif isinstance(response, (dict, list)):
        try:
            return json.dumps(response)  # Convert to JSON string
        except TypeError as e:
            logging.error(f"JSON serialization error: {e}")
            return str(response)  # Fallback to string
    else:
        return str(response)  # Fallback to string conversion

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)