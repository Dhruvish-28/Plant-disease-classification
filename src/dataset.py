{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73a13078-a046-4052-884f-9a554605d65f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from torchvision.datasets import ImageFolder\n",
    "from torchvision import transforms\n",
    "from torch.utils.data import DataLoader\n",
    "\n",
    "train_transforms = transforms.Compose([\n",
    "    transforms.Resize((224,224)),\n",
    "    transforms.RandomHorizontalFlip(),\n",
    "    transforms.RandomRotation(30),\n",
    "    transforms.ToTensor(),\n",
    "    transforms.Normalize(\n",
    "        mean = [0.485,0.456,0.406],\n",
    "        std=[0.229,0.224,0.225]\n",
    "    )\n",
    "])\n",
    "\n",
    "val_transforms = transforms.Compose([\n",
    "    transforms.Resize((224,224)),\n",
    "    transforms.ToTensor(),\n",
    "    transforms.Normalize(\n",
    "        mean = [0.485,0.456,0.406],\n",
    "        std=[0.229,0.224,0.225]\n",
    "    )\n",
    "])\n",
    "\n",
    "\n",
    "\n",
    "dataset = ImageFolder(root=data_dir, transform=train_transforms)\n",
    "\n",
    "from torch.utils.data import random_split\n",
    "\n",
    "train_size = int(0.7 * len(dataset))\n",
    "val_size = int(0.15 * len(dataset))\n",
    "test_size = len(dataset) - train_size - val_size\n",
    "\n",
    "train_dataset, val_dataset, test_dataset = random_split(\n",
    "    dataset, [train_size, val_size, test_size]\n",
    ")\n",
    "\n",
    "val_dataset.dataset.transform = val_transforms\n",
    "test_dataset.dataset.transform = val_transforms\n",
    "\n",
    "\n",
    "\n",
    "train_loader = DataLoader(\n",
    "    train_dataset, batch_size = 64 , shuffle = True , num_workers=4, pin_memory=True\n",
    ")\n",
    "\n",
    "val_loader = DataLoader(\n",
    "    val_dataset , batch_size = 64, shuffle = False , num_workers=4, pin_memory=True\n",
    ")\n",
    "\n",
    "test_loader = DataLoader(\n",
    "    test_dataset, batch_size=64, shuffle=False, num_workers=4, pin_memory=True\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
