
import threading
import numpy
import opennsfw2
from PIL import Image
from keras import Model

from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.85


def get_predictor() -> Model:
    return None  # Thay vì trả về mô hình, hàm này sẽ trả về None

def clear_predictor() -> None:
    pass  # Bỏ trống hàm này hoặc bạn có thể xóa nó đi

def predict_frame(target_frame: Frame) -> bool:
    return False  # Thay vì dự đoán, hàm này luôn trả về False

def predict_image(target_path: str) -> bool:
    return False  # Thay vì dự đoán, hàm này luôn trả về False

def predict_video(target_path: str) -> bool:
    return False  # Thay vì dự đoán, hàm này luôn trả về False
