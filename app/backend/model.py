import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from pathlib import Path

import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from pathlib import Path


class PlantDiseaseCNN(nn.Module):

    def __init__(self, num_classes=38):
        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(128 * 28 * 28, 512),
            nn.ReLU(),
            nn.Dropout(0.5),

            nn.Linear(512, num_classes)
        )

    def forward(self, x):

        x = self.features(x)
        x = self.classifier(x)

        return x

class PlantDiseaseClassifier:
    """PyTorch model for plant disease classification"""
    
    def __init__(self, model_path, classes):
        """
        Initialize the classifier
        
        Args:
            model_path: Path to the trained PyTorch model
            classes: List of disease class names
        """
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.classes = classes
        self.model_path = model_path
        self.model = None
        self.loaded = False
        
        # Define the preprocessing pipeline
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
        
        self.load_model()
    
    def load_model(self):
        """Load the trained model"""
        try:
            if not Path(self.model_path).exists():
                raise FileNotFoundError(f"Model file not found: {self.model_path}")
            
            # Load model - adjust architecture based on your specific model
            # This assumes a ResNet50 or similar architecture
            self.model = PlantDiseaseCNN(num_classes=len(self.classes))

            self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
            
            self.model.to(self.device)
            self.model.eval()
            self.loaded = True
            print(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    def preprocess_image(self, image_path):
        """Preprocess image for model inference"""
        try:
            image = Image.open(image_path).convert('RGB')
            tensor = self.transform(image)
            return tensor.unsqueeze(0).to(self.device)
        except Exception as e:
            raise ValueError(f"Error preprocessing image: {e}")
    
    def classify(self, image_path):
        """
        Classify a plant disease from an image
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary with classification results
        """
        if not self.loaded:
            return {'error': 'Model not loaded'}
        
        try:
            # Preprocess image
            image_tensor = self.preprocess_image(image_path)
            
            # Run inference
            with torch.no_grad():
                outputs = self.model(image_tensor)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                confidence, predicted = torch.max(probabilities, 1)
            
            # Get results
            predicted_class = self.classes[predicted.item()]
            confidence_score = confidence.item()
            
            # Get all class probabilities for confidence breakdown
            all_probs = probabilities[0].cpu().numpy()
            class_probabilities = {
                self.classes[i]: float(all_probs[i])
                for i in range(len(self.classes))
            }
            
            return {
                'disease': predicted_class,
                'confidence': round(confidence_score, 4),
                'confidence_percentage': round(confidence_score * 100, 2),
                'all_predictions': class_probabilities
            }
        
        except Exception as e:
            return {'error': f'Classification failed: {str(e)}'}
