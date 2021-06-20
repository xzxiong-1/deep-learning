
import numpy as np 
from torch.utils.data import DataLoader,Dataset

class RandomDataset(Dataset):
    def __getitem__(self, index):
        return np.random.randin(0, 1000, 3)

    def __len__(self):
        return 16

          
dataset = RandomDataset()
dataloader = DataLoader(dataset, batch_size=2, num_workers=4)
for batch in dataloader:
    print(batch)
