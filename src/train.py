{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3dc7a15-8f25-4ef9-a1b0-dc7232de3f5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "start = time.time()\n",
    "\n",
    "num_epochs = 10\n",
    "best_val_acc = 0\n",
    "\n",
    "train_losses = []\n",
    "val_losses = []\n",
    "train_accuracies = []\n",
    "val_accuracies = []\n",
    "\n",
    "for epoch in range(num_epochs):\n",
    "\n",
    "    train_loss, train_acc = train_one_epoch(\n",
    "        model,\n",
    "        train_loader,\n",
    "        criterion,\n",
    "        optimizer,\n",
    "        device\n",
    "    )\n",
    "\n",
    "    val_loss, val_acc = validate_one_epoch(\n",
    "        model,\n",
    "        val_loader,\n",
    "        criterion,\n",
    "        device\n",
    "    )\n",
    "\n",
    "    print(f\"Epoch {epoch+1}/{num_epochs}\")\n",
    "    print(f\"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}\")\n",
    "    print(f\"Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.4f}\")\n",
    "    print(\"-\"*40)\n",
    "\n",
    "    train_losses.append(train_loss)\n",
    "    val_losses.append(val_loss)\n",
    "    train_accuracies.append(train_acc)\n",
    "    val_accuracies.append(val_acc)\n",
    "    \n",
    "    if val_acc > best_val_acc:\n",
    "\n",
    "        best_val_acc = val_acc\n",
    "\n",
    "        torch.save(\n",
    "            model.state_dict(),\n",
    "            \"best_plant_disease_model.pth\"\n",
    "        )\n",
    "        \n",
    "end = time.time()\n",
    "print(f\"Time taken : {(end - start)/60} minutes\")\n",
    "\n",
    "model.load_state_dict(torch.load(\"best_plant_disease_model.pth\", weights_only=True))\n",
    "model.eval()"
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
