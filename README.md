# DALL-E Image Generation Tool

This is a Streamlit-based web application that allows users to generate images using OpenAI's DALL-E 3 model. The app provides an interface for users to input image descriptions and generate images accordingly.

## Features

- **Image Generation**: Generate images based on textual descriptions using OpenAI's DALL-E 3 model.
- **User Interface**: Simple and intuitive interface powered by Streamlit.
- **Customization**: Choose the number of images to generate (1-10).

## Requirements

- Python 3.8 or higher
- Streamlit
- OpenAI Python client library
- PIL (Python Imaging Library)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add Your OpenAI API Key**:
    - Replace the placeholder `<your-api-key-from-OPEN-AI>` in the `apikey.py` file with your actual OpenAI API key.

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser (the default URL is `http://localhost:8501`).

2. Enter a description for the image you want to generate in the input box.

3. Select the number of images to generate using the slider.

4. Click on the "Generate Images" button to create the images. The generated images will be displayed below the button.

## Files

- **app.py**: Main script containing the Streamlit app logic.
- **apikey.py**: Script containing the API key for OpenAI (make sure to replace the placeholder with your actual key).

## Acknowledgements

- OpenAI for providing the powerful DALL-E 3 model.
- Streamlit for creating an easy-to-use framework for building web apps with Python.
