# Snow Pole Detection — TDT4265 Mini-Project
**Course:** TDT4265 Computer Vision and Deep Learning, NTNU 2026  
**Task:** Snow Pole Detection with images from Trondheim

## Overview
Real-time detection of snow poles using YOLO11s, trained on two datasets 
captured in the Trøndelag region. Snow poles are used to localize roads 
in winter conditions. 

## What I Learned
- Data augmentation techniques (mosaic, HSV shift, etc.) and their effect on mAP in low-data regimes
- Trade-offs between dataset quality/consistency vs. size (dashcam vs. iPhone footage results)
- Fine-tuning YOLO11 architectures and interpreting precision/recall/mAP metrics
- Project built for the course TDT4265, gaining a 3rd place finish of over 80 contestants.

<img width="1920" height="1228" alt="val_batch1_pred(1)" src="https://github.com/user-attachments/assets/7c5c84a5-eb75-413d-ab7c-2b5eb13784cf" />


## Results

| Dataset | Leaderboard Score | Precision | Recall | mAP@50 | mAP@0.5:0.95 |
|---|---|---|---|---|---|
| roadpoles_v1 | 73.7 | 0.915 | 0.938 | 0.973 | 0.696 |
| Road_Poles_iPhone | 80.18 | 0.964 | 0.994 | 0.989 | 0.849 |

## Datasets
- **roadpoles_v1** — 322 train, 92 validation, 46 test images. Dashcam footage, 1920×1208px PNG
- **Road_Poles_iPhone** — 942 train, 261 validation, 138 test images. iPhone footage, 1080×1920px JPEG

## Model
- Architecture: YOLO11s (small), pretrained on COCO, fine-tuned on Poles2025

## Training Setup
- Platform: Google Colab Pro (NVIDIA A100 SXM4 80GB)
- Framework: Ultralytics 8.4.x / PyTorch
