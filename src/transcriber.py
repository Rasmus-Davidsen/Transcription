from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self, model):
        print(f"Loading Faster Whisper ({model})")

        self.model = WhisperModel(
            model, device = "cpu", compute_type = "int8"
        )

    def transcribe(self, file_path):
        segments, _ = self.model.transcribe(
            file_path,
            beam_size=1, 
            vad_filter=True,
            condition_on_previous_text=False
        )

        return segments