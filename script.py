import os
import subprocess

# Path to your dataset
DATASET_DIR = "C:\\Users\\khaws\\Desktop\\AVD_EDI\\AVD_EDI\\Reinke Ödem"
OUTPUT_DIR = "C:\\Users\\khaws\\Desktop\\AVD_EDI\\AVD_EDI\\Reinke Ödem converted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_to_wav(input_file, output_file):
    # sox can usually read .nsp/.egg if Snack is installed
    # Change rate/encoding if needed
    cmd = ["sox.exe", input_file, "-r", "16000", "-e", "signed-integer", output_file]
    subprocess.run(cmd, check=True)

for root, _, files in os.walk(DATASET_DIR):
    for f in files:
        if f.endswith(".nsp"):   # or ".egg" if you want EGG waveform
            input_path = os.path.join(root, f)
            output_path = os.path.join(
                OUTPUT_DIR, os.path.splitext(f)[0] + ".wav"
            )
            try:
                convert_to_wav(input_path, output_path)
                print(f"Converted {input_path} -> {output_path}")
            except Exception as e:
                print(f"Error converting {input_path}: {e}")
