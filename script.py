import os
import subprocess

BASE_DIR = "/home/manthan/AVD_EDI"
FOLDERS = ["Phonationsknötchen", "Stimmlippenkarzinom", "Stimmlippenpolyp"]

def convert_nsp_to_wav(input_file, output_file):
    # FFmpeg can treat .nsp as raw PCM 16-bit little-endian
    cmd = [
        "ffmpeg",
        "-f", "s16le",      # 16-bit PCM
        "-ar", "16000",     # sample rate
        "-ac", "1",         # mono
        "-i", input_file,   # input
        output_file         # output
    ]
    subprocess.run(cmd, check=True)

for folder in FOLDERS:
    dataset_dir = os.path.join(BASE_DIR, folder)
    output_dir = os.path.join(BASE_DIR, folder + "_converted")
    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(dataset_dir):
        for f in files:
            if f.endswith(".nsp"):
                input_path = os.path.join(root, f)
                output_path = os.path.join(
                    output_dir,
                    os.path.splitext(f)[0] + ".wav"
                )
                try:
                    convert_nsp_to_wav(input_path, output_path)
                    print(f"Converted {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Error converting {input_path}: {e}")

