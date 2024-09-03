from torch import cuda
import torch

print('Cuda version on your computer: \n',cuda.get_device_name(cuda.current_device()))
print('Torch version:\n',torch.__version__)

x = torch.rand(2, 3) 

print('If there are numbers here it works:\n',x)