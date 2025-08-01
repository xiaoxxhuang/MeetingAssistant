from llama_cpp import Llama

# Replace the path below with the path to your downloaded GGUF model.
model_path = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

llm = Llama(model_path=model_path, n_gpu_layers=0)

prompt = "What is the capital of France?"
response = llm(prompt, max_tokens=32, echo=False)
print(response["choices"][0]["text"].strip())
