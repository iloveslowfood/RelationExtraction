import os
from dataclasses import dataclass
import torch


TRAIN = "./input/data/train/train.tsv"
TEST = "./input/data/test/test.tsv"
LABEL = "./input/data/label_type.pkl"
LOGS = "./logs"
CKPT = "./saved_models"

DOT = "."


@dataclass
class Config:
    """notebooks 디렉토리의 주피터 환경에서 아래의 configuration을 활용할 수 있도록 구성
    DOT + SOMETHING: '../something/something' <- 디렉토리 경로를 바꿔주게 됨
    """

    Train: str = TRAIN if os.path.isfile(TRAIN) else DOT + TRAIN
    Test: str = TEST if os.path.isfile(TEST) else DOT + TEST
    ValidSize: float = 0.1
    Label: str = LABEL if os.path.isfile(LABEL) else DOT + LABEL
    Logs: str = LOGS if os.path.isfile(LOGS) else DOT + LOGS
    NumClasses: int = 42
    Epochs: int = 3

    Batch8:int = 8
    Batch16: int = 16
    Batch32: int = 32
    Batch64: int = 64

    LRFaster: float = 0.01
    LRFast: float = 0.005
    LR: float = 0.001
    LRSlow: float = 0.0005
    LRSlower: float = 0.0001

    Seed: int = 42
    Device: str = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    CheckPoint: str = "./saved_models"
    SavePath: str = "./predictions"


@dataclass
class Optimizer:
    Adam: str = "Adam"
    AdamP: str = "AdamP"
    SGD: str = "SGD"
    Momentum: str = "Momentum"
    CosineScheduler: str = "CosineScheduler"


@dataclass
class Loss:
    CE: str = "crossentropyloss"
    LS: str = "labelsmoothingLoss"


@dataclass
class PreProcessType:
    Base: str = "Base" # No preprocessing => 구려
    ES: str = 'EntitySeparation' # Entity Separation, method as baseline of boostcamp itself
    ESP: str = 'ESPositionEmbedding' # Entity Separation with Position Embedding, add scalar for each values in entities
    EM: str = "EntityMarker"  # Entity Marking


@dataclass
class ModelType:
    VanillaBert: str = 'VanillaBert'
    Base: str = "BertModel"
    SequenceClf: str = "BertForSequenceClassification"


@dataclass
class PreTrainedType:
    BertMultiLingual: str = "bert-base-multilingual-cased"