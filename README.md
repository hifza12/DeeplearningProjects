
## Cotton Plant Disease Prediction Using Transfer Learning Approaches 


This repository contains code for predicting cotton plant diseases using transfer learning approaches. Transfer learning is a popular technique in deep learning that involves using a pre-trained model as a starting point for a new task.


## Background

Cotton is an important crop that is grown worldwide for its fiber, seed, and oil. However, cotton plants are susceptible to a number of diseases that can significantly reduce crop yields. Identifying and treating these diseases early is critical for ensuring healthy crops and maintaining productivity.

In recent years, deep learning has emerged as a powerful tool for image analysis and has been applied to a wide range of problems, including plant disease diagnosis. Transfer learning, in particular, has been shown to be effective for plant disease classification tasks.

## Data
The dataset used in this project is the Cotton Plant Disease dataset, which contains images of healthy cotton plants as well as plants affected by three common diseases: leaf curl, fullsurim and wilt. The dataset contains 2500 images for each class, for a total of 500 images. and similarly dataset contains test and validation data as well.

## Approach
Transfer learning is used in this project to fine-tune a pre-trained model for cotton plant disease classification. Specifically, the InceptionV3 model, which has been pre-trained on the ImageNet dataset, is used as a starting point. The final layer of the model is replaced with a new layer that is trained to classify the four different diseases. after that different transfer learning model has been implemented to test the performance of the model such as Vgg16, Resnet,Vgg19 and mobilenet, we observed that with mobilenet we get better performance of the model on both testing and training data and get generalized model. 

The model is trained using a combination of data augmentation and fine-tuning. Data augmentation is used to generate additional training examples by applying random transformations to the input images. Fine-tuning involves training the entire model on the new task, with a low learning rate to avoid overfitting.

## Results
The trained model achieves an accuracy of 96% on a held-out test set, demonstrating that transfer learning is an effective approach for cotton plant disease prediction.

# Usage
To use this code, first clone the repository:


git clone https://github.com/hifza12/cotton-plant-disease-prediction.git

## Future Work
There are several ways in which this project could be extended. For example, the dataset could be expanded to include more types of diseases or different plant species. Additionally, the performance of the model could be improved by using more advanced techniques such as ensembling or transfer learning from multiple pre-trained models.

