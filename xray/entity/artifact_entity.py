from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader


@dataclass
class DataIngestionArtifacts:
    train_file_path: str 
    test_file_path: str
