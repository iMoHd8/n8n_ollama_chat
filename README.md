# n8n Ollama Chat

FastAPI-based backend with local LLMs (Ollama) and integrating with n8n webhooks.

## Project Structure
```
backend/
  main.py             # Main FastAPI endpoint
  UI.py               # Main Streamlit app entry point
  config.py             # Configuration settings
assets/               # Screenshots from the application  
requirements.txt      # Python dependencies
n8n_ollama_chat_workflow.json    # n8n workflow file in JSON
```


## Getting Started

### Prerequisites
- Python 3.12+
- Required Python packages (see `requirements.txt`)
- [Ollama](https://ollama.com/) running locally (default port: `11434`) must be [installed](https://ollama.com/download) and running on your machine
- The `gemma3:latest` model must be pulled using Ollama, or chose any other model from [ollama models](https://ollama.com/search)
    - If you choose another model, you must change the model ID in the `config.py` file.

    ```powershell
    ollama pull gemma3
    ```

- [n8n](https://n8n.io/) running locally (default port: `5678`)

---

### Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/iMoHd8/n8n_ollama_chat.git
   cd n8n_ollama_chat
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Install Ollama:
    - Visit [Ollama Website](https://ollama.com/download)
    - Install for your OS (macOS, Windows, or Linux)

4. Run a local LLM:
    - Open terminal and run a model:
    ```powershell
    ollama run gemma3
    ```
    - This will download and run the model locally (it runs a local API at http://localhost:11434/api/generate)

5. Start n8n locally: (Make sure [Node.js](https://nodejs.org/en/download) is installed on your local machine)
    ```powershell
    cd backend
    npx n8n
    ```
    - This will run n8n locally at http://localhost:5678
    - From n8n dashboard:
        - Create Workflow
        - From the workflow option, select `import from File...`
        - Select the `n8n_ollama_chat_workflow.json` file


    ![n8n_workflow](assets\n8n_workflow.png)


6. Start the FastAPI Backend
    ```powershell
    cd backend
    uvicorn main:app --reload
    ```
    - This will run FastAPI locally at http://localhost:8000
        - or visit http://localhost:8000/docs for the Swagger UI
    

### Running the Application
### Option 1:
You can run the application using the command line or any terminal:

To run the workflow in production:
```powershell
curl.exe -X POST -H "Content-Type: application/json" -d '{\"prompt\": \"What is the capital of Jordan?\"}' http://localhost:5678/webhook/generate
```

or run the workflow in test mode:
- click on `Execute workflow` from the n8n workflow dashboard

-  ```powershell
    curl.exe -X POST -H "Content-Type: application/json" -d '{\"prompt\": \"What is the capital of Jordan?\"}' http://localhost:5678/webhook-test/generate
    ```
- Change the query ("What is the capital of Jordan?") to any question you want


### Option 2
You can run the application using Streamlit UI:
1. Start the Streamlit app:
   ```powershell
   streamlit run UI.py
   ```

2. Send You question, and wait for the answer...

    ![Strealit_demo](assets\Streamlit_UI.png)

## Customization
- Modify `config.py` to adjust the ollama model id.



## Troubleshooting
- 422 Unprocessable Entity: Ensure your JSON body is correctly formatted and includes the prompt field.
- Connection Errors: Make sure Ollama and the FastAPI server are running and accessible.