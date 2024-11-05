# import streamlit as st
# import os
# import torch
# from torchvision.transforms import transforms
# from PIL import Image
# from pathlib import Path


# # this is for saving images and prediction
# def save_image(uploaded_file):
#     if uploaded_file is not None:
#         save_path = os.path.join("images", "input.jpeg")
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.read())
#         st.success(f"Image saved to {save_path}")

#         model = torch.load(Path('model/model.pt'))


#         trans = transforms.Compose([
#             transforms.RandomHorizontalFlip(),
#             transforms.Resize(224),
#             transforms.CenterCrop(224),
#             transforms.ToTensor(),
#             ])

#         image = Image.open(Path('images/input.jpeg'))

#         input = trans(image)

#         input = input.view(1, 1, 224, 224).repeat(1, 3, 1, 1)

#         output = model(input)

#         prediction = int(torch.max(output.data, 1)[1].numpy())
#         print(prediction)

#         if (prediction == 0):
#             print ('Normal')
#             st.text_area(label="Prediction:", value="Normal", height=100)
#         if (prediction == 1):
#             print ('PNEUMONIA')
#             st.text_area(label="Prediction:", value="PNEUMONIA", height=100)

# if __name__ == "__main__":
#     st.title("Xray lung classifier")
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
#     save_image(uploaded_file)

    
import streamlit as st
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path
import os

# Function to process the uploaded image and give prediction
def process_image(uploaded_file):
    if uploaded_file is not None:
        # Load the image directly from the uploaded file (no saving to disk)
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Check if the model file exists
        model_path =  torch.load(Path('C:/Users/riswa/Desktop/AI/XRay/xray/ml/model/model.pt'))

        if not model_path.exists():
            st.error(f"Model file not found: {model_path}")
            return

        # Load the pre-trained model
        model = torch.load(model_path)

        # Define the image transformations
        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
        ])

        # Apply the transformations to the uploaded image
        input_tensor = trans(image)

        # Adjust the input tensor to match the expected input dimensions of the model
        input_tensor = input_tensor.view(1, 1, 224, 224).repeat(1, 3, 1, 1)

        # Make the prediction using the loaded model
        output = model(input_tensor)

        # Extract the predicted class
        prediction = int(torch.max(output.data, 1)[1].numpy())

        # Display the prediction result
        if prediction == 0:
            st.success("Prediction: Normal")
        elif prediction == 1:
            st.error("Prediction: PNEUMONIA")
        else:
            st.warning("Prediction: Unknown result")

if __name__ == "__main__":
    st.title("X-ray Lung Classifier")

    # Upload the image through Streamlit's file uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    # Call the function to process the uploaded image
    if uploaded_file is not None:
        process_image(uploaded_file)
