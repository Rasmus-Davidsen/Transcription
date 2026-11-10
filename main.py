import sys
import os

from src.audio_processor import AudioProcessor

def main():
    # Validate source directory
    if len(sys.argv) < 2:
        print("Missing source directory parameter")
        return

    src_dir = sys.argv[1]

    if not os.path.exists(src_dir) or not os.path.isdir(src_dir):
        print("No such source directory: " + src_dir)
        return

    # Validate target directory
    if len(sys.argv) < 3:
        print("Missing target directory parameter")
        return

    target_dir = sys.argv[2]

    processor = AudioProcessor(
        "small", # Much faster with minimal loss in accuracy
        "en_core_web_sm"
    )

    processor.process_dir(
        src_dir, target_dir
    )

if __name__ == "__main__":
    main()