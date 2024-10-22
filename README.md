# Carpet-Defect-Classification

## Overview
The Carpet-Defect-Classification project aims to distinguish defective carpets from perfect ones by utilizing the VGG16 model, a widely used convolutional neural network (CNN) architecture. The project implements a modular pipeline for training and deployment, leveraging deep learning techniques for image classification. Additionally, it integrates Continuous Integration (CI) and Continuous Deployment (CD) processes through AWS services and GitHub Actions."

## Dataset
The dataset used for this project is sourced from the [MVTec Anomaly Detection Dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad/downloads), which contains images for defect detection across various categories, including textiles like carpets.

## Project Workflow

### Steps to run the project:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/abbykabraham/Carpet-Defect-Classification.git
    cd Carpet-Defect-Classification
    ```

2. **Create a Conda Environment**
    Create a new Conda environment and activate it:
    ```bash
    conda create -n carpetcls python=3.11 -y
    conda activate carpetcls
    ```

3. **Install Dependencies**
    Install all the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**
    To start the application and model training:
    ```bash
    python app.py
    ```

5. **Access the Application**
    After running the above command, access the app through the local host and port assigned by Flask.

### DVC (Data Version Control) Commands
This project uses DVC for tracking datasets and managing the model training pipeline.

1. **Initialize DVC**:
    ```bash
    dvc init
    ```

2. **Run the Pipeline**:
    Reproduce the pipeline stages to train the model and manage data dependencies:
    ```bash
    dvc repro
    ```
## AWS CI/CD Pipeline with GitHub Actions

### Steps for Deployment

1. **Login to AWS Console**
    - Login to your AWS console and create an IAM user with necessary permissions.

2. **AWS Resources Used**:
    - **EC2 (Elastic Compute Cloud)**: Used for launching virtual machines.
    - **ECR (Elastic Container Registry)**: For storing Docker images of the application.

3. **Deployment Process**:
    - **Build the Docker Image**: Dockerize the application and push the image to Amazon ECR.
    - **Launch EC2**: Start an EC2 instance to host the application.
    - **Pull the Image**: Pull the Docker image from ECR into EC2.
    - **Run the Container**: Deploy and run the Docker container on the EC2 instance.

### Policies and Permissions
Ensure the following policies are attached to your IAM user:

- **AmazonEC2ContainerRegistryFullAccess**: Grants full access to ECR.
- **AmazonEC2FullAccess**: Grants full access to EC2.

### Steps for Docker Setup on EC2

1. **Install Docker**:
    Update and install Docker on the EC2 instance:
    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

2. **Setup Self-hosted GitHub Runner**:
    - Configure the EC2 instance as a self-hosted runner for GitHub Actions. This will enable CI/CD integration directly on your EC2 instance.
    - Go to GitHub repository settings, and follow the steps under `Actions > Runners > New self-hosted runner`.

3. **Setup GitHub Secrets**:
    - Add your AWS credentials and other necessary information in GitHub secrets for secure access during deployment.

## Additional Details

- **Config Files**: 
    - `config.yaml`: Contains configurations related to data paths, model preparation, callback settings, and training parameters. 
    - `params.yaml`: Defines hyperparameters for model training.