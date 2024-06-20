# Shape Detection and Classification using YOLO and ResNet

Welcome to my project on shape detection and classification, developed for my Computational Intelligence lesson. This repository includes scripts for generating random shapes, training a YOLO model for object detection, and training a custom ResNet model for shape classification.

## Project Structure

- **annotations.csv**: CSV file containing annotations for generated images.
- **shape_counts.csv**: CSV file with counts of circles, rectangles, and triangles for each image.
- **yolov8n.pt**: Pre-trained YOLO model weights used for training.

### Folders

- **result/**: Contains generated random shape images.

### Scripts and Notebooks

- **Shape_Generation.py**: Python script for generating random shapes and saving annotations.
- **Yolo_Train.ipynb**: Jupyter Notebook for YOLO model training.
- **Yolo_val.ipynb**: Jupyter Notebook for YOLO model validation.
- **Resnet_Train.ipynb**: Jupyter Notebook for ResNet model training.
- **Resnet_val.ipynb**: Jupyter Notebook for ResNet model validation.

## How to Use

### Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd Shape-Detection-Classification-YOLO-ResNet


Generate Shapes
Run the Shape_Generation.py script to create the dataset of random shapes and their annotations.

bash
Copy code
python Shape_Generation.py
Train YOLO Model
Open and execute the Yolo_Train.ipynb notebook to train the YOLO model using the generated dataset.

Train ResNet Model
Open and execute the Resnet_Train.ipynb notebook to train the custom ResNet model on the generated dataset.

Evaluate Models
Use the respective validation notebooks (Yolo_val.ipynb and Resnet_val.ipynb) to evaluate the trained models.