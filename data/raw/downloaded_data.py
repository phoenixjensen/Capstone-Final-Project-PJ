import kagglehub

path = kagglehub.dataset_download(
    "raminhuseyn/demand-forecasting-dataset",
    output_dir="./data/demand-forecasting"
)

print("Path to dataset files:", path)
