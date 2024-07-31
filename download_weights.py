import requests
url = "https://github.com/ultralytics/yolov5s/releases/download/v8.0.0/yolov5s.pt"
response = requests.get(url)
with open("yolov5s.pt", "wb") as f:
    f.write(response.content)

    print("Download completed!")