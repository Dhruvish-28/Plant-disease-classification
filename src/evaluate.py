{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9d2a21d-7311-4629-9a96-3d25e9c365c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "model.load_state_dict(torch.load(\"best_plant_disease_model.pth\", weights_only=True))\n",
    "model.eval()\n",
    "test_loss, test_acc = validate_one_epoch(\n",
    "    model,\n",
    "    test_loader,\n",
    "    criterion,\n",
    "    device\n",
    ")\n",
    "\n",
    "print(\"Test Accuracy:\", test_acc)\n",
    "print(\"Test Loss:\", test_loss)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a307c2d-de69-4fdb-be6a-1a7b0ef7f21e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "epochs = range(1, len(train_losses) + 1)\n",
    "\n",
    "# Loss curves\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.plot(epochs, train_losses, label=\"Train Loss\")\n",
    "plt.plot(epochs, val_losses, label=\"Validation Loss\")\n",
    "plt.xlabel(\"Epoch\")\n",
    "plt.ylabel(\"Loss\")\n",
    "plt.title(\"Training vs Validation Loss\")\n",
    "plt.legend()\n",
    "plt.show()\n",
    "\n",
    "# Accuracy curves\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.plot(epochs, train_accuracies, label=\"Train Accuracy\")\n",
    "plt.plot(epochs, val_accuracies, label=\"Validation Accuracy\")\n",
    "plt.xlabel(\"Epoch\")\n",
    "plt.ylabel(\"Accuracy\")\n",
    "plt.title(\"Training vs Validation Accuracy\")\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a32dd807-6b5c-495d-8220-32e6b5a5e71a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "\n",
    "all_preds = []\n",
    "all_labels = []\n",
    "\n",
    "model.eval()\n",
    "\n",
    "with torch.no_grad():\n",
    "    for images, labels in test_loader:\n",
    "        images = images.to(device)\n",
    "        labels = labels.to(device)\n",
    "\n",
    "        outputs = model(images)\n",
    "        _, preds = torch.max(outputs, 1)\n",
    "\n",
    "        all_preds.extend(preds.cpu().numpy())\n",
    "        all_labels.extend(labels.cpu().numpy())\n",
    "\n",
    "cm = confusion_matrix(all_labels, all_preds)\n",
    "\n",
    "import seaborn as sns\n",
    "\n",
    "plt.figure(figsize=(12,10))\n",
    "sns.heatmap(cm, cmap=\"Blues\", xticklabels=dataset.classes, yticklabels=dataset.classes)\n",
    "plt.xlabel(\"Predicted\")\n",
    "plt.ylabel(\"Actual\")\n",
    "plt.title(\"Confusion Matrix\")\n",
    "plt.show()"
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
