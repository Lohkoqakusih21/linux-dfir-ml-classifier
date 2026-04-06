import os
import math

def calculate_entropy(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        if not data:
            return 0
        entropy = 0
        for x in range(256):
            p_x = data.count(bytes([x])) / len(data)
            if p_x > 0:
                entropy -= p_x * math.log2(p_x)
        return entropy
    except:
        return 0


def extract_features(file_path):
    try:
        size = os.path.getsize(file_path)
        entropy = calculate_entropy(file_path)

        return {
            "file_path": file_path,
            "size": size,
            "entropy": entropy
        }
    except:
        return None