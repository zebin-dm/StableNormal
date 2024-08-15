import torch

device = torch.device("cuda:0")
data = torch.rand(5, 3)
data.to(device)
