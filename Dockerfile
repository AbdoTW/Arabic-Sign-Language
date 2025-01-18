# Base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && apt-get clean

RUN pip install --upgrade pip

# Install PyTorch, TorchVision, and TorchAudio with CUDA 11.8 support
# Adjust your CUDA version here 
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --timeout 1000
RUN pip install ultralytics
RUN pip install arabic_reshaper
RUN pip install python-bidi

# copy files to container 
COPY best_ASL.pt .
COPY functions.py .
COPY Arabic_Sign_Language_Recognition.py .

CMD ["python", "Arabic_Sign_Language_Recognition.py"]