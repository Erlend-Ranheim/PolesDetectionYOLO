from ultralytics import YOLO
def trainModel():

    model = YOLO("yolo11n.pt")
    model.train(
        data="Datasets/roadpoles_v1/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
    )

if __name__ == '__main__':
    trainModel()

