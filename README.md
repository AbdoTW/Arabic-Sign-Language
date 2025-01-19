# Arabic Sign Language Real-Time Recognition

![Project Banner](Files/ASL.gif)

## Overview

This project is a real-time detection system for Arabic Sign Language made by YOLOv10

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Demo](#demo)
4. [Installation](#installation)
5. [Results](#results)

## Introduction

Arabic Sign Language(ASL): A visual-gestural language used by deaf and hard of hearing communities primarily in our Arabian words. Just like spoken languages

![ASL](Files/Images/Signs.png)

- Dataset: [Link Text](https://www.kaggle.com/datasets/ammarsayedtaha/arabic-sign-language-dataset-2022)
- Kaggle Notebook: [Link Text](https://www.kaggle.com/code/abdalrhmantwfik/arabic-sign-language-arsl-yolov10m)


## Features

- The ASL detection system is able to detect the gestures by predicting the boundary box of where the gesture is and what it describes as a label
- Works on Real-Time inference
- Utilizes any webcam to apply the inference

## Demo

![Demo](Files/ASL_Demo_readme.gif)

## Installation (how to use ?)
- 1- create a conda environment with python version 3.10 
```bash
 conda create --name arabic_sing_language python=3.10
```
- 2- activate this environment
```bash
 conad activate arabic_sign_language
```
- 2- install pytorch with supporting GPU [Setup NVIDIA GPU for PyTorch](https://youtu.be/r7Am-ZGMef8?si=mBBcznTvfpIOPRCa)
```bash
 conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
``` 
- 3- install some packages 
```bash
 conda install -c conda-forge ultralytics -y
 conda install -c conda-forge arabic_reshaper -y
 conda install -c conda-forge python-bidi
```
- 4- use this command to run the project (make sure the camera is open)
```bash
 python Arabic_Sign_Language_Recognition.py
```

## Results

- Metrics

![Metrics](Files/Images/confusion_matrix.png)
![Metrics](Files/Images/f1_score.png)
![Metrics](Files/Images/precision.png)
![Metrics](Files/Images/recall.png)
![Metrics](Files/Images/scores.png)

- Predictions
![Predictions](Files/Images/predictions.png)

