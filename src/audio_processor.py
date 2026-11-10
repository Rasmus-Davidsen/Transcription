import os
import csv

from src.transcriber import Transcriber
from src.analyser import Analyser

def normalize(word):
    word = word.lower()
    
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('?', '')
    word = word.replace('!', '')

    return word

class AudioProcessor:
    def __init__(self, whisperModel, spacyModel):
        self.transcriber = Transcriber(whisperModel)
        self.analyser = Analyser(spacyModel)

    def process_dir(self, src_dir, target_dir):
        os.makedirs(target_dir, exist_ok=True)

        # Create or clear file
        with open(target_dir + "/transcription.txt", "w") as file:
            pass

        words = {}
        
        for file in os.listdir(src_dir):
            if file.endswith(".mp3"):
                file_path = src_dir + "/" + file

                self.process_file(
                    words, target_dir, file_path
                )

        self.export_words(words, target_dir)

    def process_file(self, words, target_dir, file_path):
        print("Processing " + file_path)

        with open(target_dir + "/transcription.txt", "a") as file:
            for segment in self.transcriber.transcribe(file_path):
                file.write(segment.text.strip() + "\n")

                for word in segment.text.split():
                    word = normalize(word)

                    count = words.get(word, 0)
                    words[word] = count + 1

    def export_words(self, words, target_dir):
        print("Exporting words to " + target_dir + "/words.csv")

        rows = []
        
        for word, count in words.items():
            pos = self.analyser.identify_pos(word)

            rows.append({
                "Word": word,
                "Occurrences": count,
                "Part of Speech": pos
            })

        with open(target_dir + "/words.csv", 'w', newline='') as file:
            columns = [
                "Word", "Occurrences", "Part of Speech"
            ]

            writer = csv.DictWriter(
                file, delimiter = ';', fieldnames = columns
            )

            writer.writeheader()
            writer.writerows(rows)