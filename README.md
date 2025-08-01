# MeetingAssistant

This project demonstrates how to set up and run a small language model on a MacBook Air (M2, 16GB RAM) using Python.

## Requirements
- macOS 13 or later
- Xcode command line tools
- Python 3.10+

## Installation
1. Install Homebrew from [https://brew.sh](https://brew.sh) if not already available.
2. Install Python and upgrade `pip`:
   ```bash
   brew install python@3.10
   pip3 install --upgrade pip
   ```
3. Install the `llama-cpp-python` package compiled with OpenBLAS:
   ```bash
   pip3 install llama-cpp-python==0.2.11
   ```
4. Download a GGUF model compatible with `llama.cpp`. For example, you can use one of the 7B models from the HuggingFace Hub. Place the model file in the `models/` directory.

## Running the Demo
1. Update `model_path` inside `local_llm_demo.py` to point to the downloaded `.gguf` file.
2. Run the script:
   ```bash
   python3 local_llm_demo.py
   ```

The script loads the model and generates a short response to a simple prompt.

## Notes
Running large models may exceed the memory limits of a 16GB MacBook Air. Start with a quantized 4-bit model to reduce memory usage.
