{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ba2a87c-b9b4-4097-8ba3-408106ab3422",
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch.nn as nn\n",
    "\n",
    "class PlantDiseaseCNN(nn.Module):\n",
    "\n",
    "    def __init__(self, num_classes = 38):\n",
    "        super().__init__()\n",
    "\n",
    "        self.features = nn.Sequential(\n",
    "\n",
    "            nn.Conv2d(3, 32, kernel_size=3, padding = 1), # 3 = RGB(input channels) , 32 = Filters(output channels)\n",
    "            nn.ReLU(),\n",
    "            nn.MaxPool2d(2), #Divides images into half (2,2 maxpool)\n",
    "\n",
    "            nn.Conv2d(32, 64, kernel_size=3, padding = 1),\n",
    "            nn.ReLU(),\n",
    "            nn.MaxPool2d(2),\n",
    "\n",
    "            nn.Conv2d(64, 128, kernel_size=3, padding = 1),\n",
    "            nn.ReLU(),\n",
    "            nn.MaxPool2d(2),\n",
    "        )\n",
    "\n",
    "        self.classifier = nn.Sequential(\n",
    "\n",
    "            nn.Flatten(),\n",
    "            nn.Linear(128*28*28 , 512), # input and output layers dimensions \n",
    "            \n",
    "            nn.ReLU(),\n",
    "            nn.Dropout(0.5),\n",
    "            nn.Linear(512 , num_classes) # num_classes = 38 , final predicted classes\n",
    "        )\n",
    "\n",
    "    def forward(self,x):\n",
    "        x = self.features(x)\n",
    "        x = self.classifier(x)\n",
    "        return x"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10",
   "language": "python",
   "name": "py310"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
