from transformers import pipeline
import scipy.io.wavfile as wavfile
import numpy as np

def generate_music(prompt, output_file="my_music"):
    """Generate music from a text prompt."""
    music_pipe = pipeline("text-to-audio", model="facebook/musicgen-small")
    music = music_pipe(prompt)
    audio = music["audio"]
    sample_rate = music["sampling_rate"]

    # Save as WAV file
    wavfile.write(output_file + ".wav", rate=sample_rate, data=np.array(audio, dtype=np.float32))
    print(f"Music saved as '{output_file}'.wav")
