import os
import numpy as np
import soundfile as sf

DATASET_DIR = r"C:\Users\khaws\Desktop\AVD_EDI\AVD_EDI\Phonationsknötchen"
OUTPUT_DIR = r"C:\Users\khaws\Desktop\AVD_EDI\AVD_EDI\Phonationsknötchen converted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_egg(path, samplerate=16000):
    with open(path, "rb") as f:
        content = f.read()
    # Snack EGG files usually have an ASCII header ending with "\f" (form feed, 0x0C)
    try:
        split_index = content.index(b"\x0C") + 1
    except ValueError:
        raise RuntimeError("Not a valid EGG file, no header delimiter found")
    raw = content[split_index:]
    # Interpret as 16-bit signed PCM
    data = np.frombuffer(raw, dtype=np.int16)
    return data, samplerate

for root, _, files in os.walk(DATASET_DIR):
    for f in files:
        if f.endswith(".egg"):
            input_path = os.path.join(root, f)
            relative_path = os.path.relpath(root, DATASET_DIR)
            target_dir = os.path.join(OUTPUT_DIR, relative_path)
            os.makedirs(target_dir, exist_ok=True)
            output_path = os.path.join(target_dir, os.path.splitext(f)[0] + ".wav")

            try:
                data, sr = read_egg(input_path, samplerate=16000)
                sf.write(output_path, data, sr)
                print(f"Converted {input_path} -> {output_path}")
            except Exception as e:
                print(f"Error converting {input_path}: {e}")
