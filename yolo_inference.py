from ultralytics import YOLO 
import torch 

model = YOLO('models/best.pt')  

# move model to gpu 
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)
print(f"Model is using device: {next(model.model.parameters()).device}")

#analyse 
results = model.predict('input/08fd33_4.mp4',save=True)

print(results[0])
print('##################################')
for box in results[0].boxes:
    print(box)