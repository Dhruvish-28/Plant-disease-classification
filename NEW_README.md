🌿 Plant Disease Classification using Convolutional Neural Networks

!\[Python](https://img.shields.io/badge/Python-3.10-blue)

!\[PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)

!\[GPU](https://img.shields.io/badge/GPU-RTX%203060-green)

!\[Dataset](https://img.shields.io/badge/Dataset-PlantVillage-orange)

!\[License](https://img.shields.io/badge/License-MIT-lightgrey)



📌 Project Overview



This project implements a deep learning pipeline for plant disease classification using leaf images from the PlantVillage dataset.



The goal is to automatically identify plant diseases from leaf images using a Convolutional Neural Network (CNN) trained with PyTorch.



Early detection of plant diseases helps prevent large-scale agricultural losses and improves crop yield.



The project demonstrates a complete machine learning application pipeline, including:



Data preprocessing and augmentation



Class imbalance handling



CNN architecture design



GPU-accelerated training



Model evaluation and visualization



Flask-based inference API



Next.js web interface for real-time predictions



Users can upload a plant leaf image through the web interface and the system predicts the most likely disease along with a confidence score.



🌐 Web Application Demo



The project includes a web interface where users can upload plant leaf images and receive predictions instantly.



Workflow

User uploads leaf image

        ↓

Next.js frontend

        ↓

Flask API request

        ↓

PyTorch CNN inference

        ↓

Predicted disease + confidence returned

        ↓

Displayed in browser

Example Prediction Interface



\### Training vs Validation Loss

!\[Loss Curve](results/Training\_loss\_curve.png)



---



\### Training vs Validation Accuracy

!\[Accuracy Curve](results/Training\_accuracy\_curve.png)



\# 🔎 Confusion Matrix



!\[Confusion Matrix](results/confusion\_matrix.png)



\### Web Upload Interface



!\[Upload Interface](results/web\_upload\_interface.png)



\### Prediction Result



!\[Prediction Result](results/prediction\_result.png)



✨ Project Highlights



• Built a CNN model from scratch for plant disease classification

• Implemented Weighted Cross Entropy to handle class imbalance

• Achieved 97.63% test accuracy on the PlantVillage dataset

• Trained on 54,305 images across 38 classes

• Implemented GPU-accelerated training using PyTorch

• Built a Flask inference API for model deployment

• Developed a Next.js web interface for image-based prediction



🔑 Key Results

Metric	Value

Test Accuracy	97.63%

Test Loss	0.102

Dataset Size	54,305 Images

Classes	38 Plant Diseases

Training Time	~12.5 minutes (RTX 3060)

📊 Dataset



Dataset: PlantVillage

Source:

https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset



Dataset Details

Attribute	Value

Total Images	54,305

Classes	38

Image Type	RGB

Example Classes



Apple Scab



Apple Black Rot



Tomato Early Blight



Potato Late Blight



Squash Powdery Mildew



🖼 Image Processing



Images undergo the following preprocessing steps:



Resize → 224 × 224



Random Horizontal Flip



Random Rotation



Conversion to Tensor



Normalization



These transformations help improve generalization and robustness.



📂 Dataset Split

Split	Percentage

Training	70%

Validation	15%

Test	15%

⚖️ Class Imbalance Handling



The dataset contains class imbalance, where some classes contain significantly fewer samples.



Example:



Class	Samples

Potato Healthy	152

Orange Huanglongbing	5507



To mitigate this issue:



Weighted Cross Entropy Loss was used



Class weights were computed using inverse class frequency



🧠 Model Architecture



The model is implemented using PyTorch.



CNN Architecture

Input: 224 × 224 × 3



Conv2D (3 → 32, kernel=3)

ReLU

MaxPool (2×2)



Conv2D (32 → 64, kernel=3)

ReLU

MaxPool (2×2)



Conv2D (64 → 128, kernel=3)

ReLU

MaxPool (2×2)



Flatten



Fully Connected (100352 → 512)

ReLU

Dropout (0.5)



Fully Connected (512 → 38)

Architecture Summary

Layer Type	Count

Convolution Layers	3

Pooling Layers	3

Fully Connected Layers	2

Dropout Layers	1

⚙️ Training Setup

Hardware



GPU: NVIDIA RTX 3060 (12GB)



Framework



PyTorch



Hyperparameters

Parameter	Value

Epochs	10

Batch Size	64

Optimizer	Adam

Learning Rate	0.001

Loss Function	Weighted CrossEntropy

Image Size	224 × 224

Training Time

~12.5 minutes (10 epochs on RTX 3060)

📈 Training Results

Epoch	Train Accuracy	Validation Accuracy

1	77.34%	83.95%

2	85.06%	89.53%

3	88.97%	91.38%

4	91.15%	91.48%

5	92.45%	92.36%

6	94.02%	93.12%

7	94.50%	93.02%

8	94.75%	92.70%

9	95.45%	92.74%

10	96.44%	93.43%



Validation accuracy stabilizes around 93–94%, indicating strong generalization.



🧪 Final Model Performance



Evaluation on the unseen test dataset:



Metric	Value

Test Accuracy	97.63%

Test Loss	0.102

📊 Training Visualizations

Training vs Validation Loss



Training vs Validation Accuracy



These curves show:



steady reduction in training loss



stable validation performance



minimal overfitting



🔎 Confusion Matrix



Most predictions lie along the diagonal, indicating strong classification performance.



📁 Repository Structure

plant-disease-classification

│

├── src/                 # backend \& ML pipeline

│   ├── dataset.py

│   ├── model.py

│   ├── train.py

│   ├── evaluate.py

│   ├── inference.py

│   └── app.py           # Flask API

│

├── app/                 # Next.js frontend

│

├── results/

│   ├── Training\_loss\_curve.png

│   ├── Training\_accuracy\_curve.png

│   └── confusion\_matrix.png

│

├── models/              # trained model weights

│

├── requirements.txt

├── README.md

└── .gitignore

▶️ Running the Project Locally

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Train the model

python src/train.py

3️⃣ Start backend API

python src/app.py

4️⃣ Start frontend

cd app

npm install

npm run dev



Then open:



http://localhost:3000

📦 Dependencies



Main libraries used:



PyTorch



numpy



matplotlib



scikit-learn



Flask



flask-cors



Full dependency list available in requirements.txt.



🚀 Future Improvements



Potential improvements include:



Transfer learning with ResNet / EfficientNet



Hyperparameter optimization



Mobile deployment



Edge device inference



Larger agricultural datasets



💡 Skills Demonstrated



This project demonstrates practical experience in:



Deep Learning



Computer Vision



CNN Architecture Design



Data Preprocessing



GPU Training



Model Evaluation



Flask API Development



Frontend Integration (Next.js)



End-to-End ML Deployment



👤 Author



Dhruvish Parikh

B.Tech – Artificial Intelligence \& Data Science



GitHub:

https://github.com/Dhruvish-28

