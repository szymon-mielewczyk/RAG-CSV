import kagglehub

# Download latest version
path = kagglehub.dataset_download("bhavikjikadara/grocery-store-dataset")

print("Path to dataset files:", path)