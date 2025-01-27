# **AI Music Generator 🎵**

An AI-powered music generation tool that creates audio tracks from simple text descriptions. This project leverages Hugging Face's `MusicGen` model to transform your creative ideas into unique soundscapes.

## **Features**
- Generate music from descriptive text prompts (e.g., "futuristic classic music").
- Save the generated audio as `.wav` files.
- Interactive command-line interface for user-friendly input.

---

## **How It Works**
1. The user provides a descriptive text prompt (e.g., "upbeat electronic dance music").
2. The script uses Hugging Face's `facebook/musicgen-small` model to generate an audio track.
3. The output is saved as a `.wav` file.

---

---

## **Usage**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-music-generator.git
cd ai-music-generator
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run script**
```bash
python main.py
```

### **4. Generate Music**

- **Example Prompt:** `"futuristic classic music"`
- **Example Output:** `musicgen.wav`

## **Requirements**
- Python 3.8 or higher

**Required libraries:**
- `transformers`
- `scipy`
- `numpy`

---

## **Examples**
**Input Prompt:**
`"epic orchestral music with futuristic vibes"`

**Generated Output:**
Saved as `epic_orchestral.wav`.

---

## **Future Plans**
- Integrate a graphical interface for easier interaction.
- Expand CLI options for advanced users (e.g., note duration, chords, duration).

---

## **Acknowledgments**
- Hugging Face for the `MusicGen` model.
- Open-source libraries like `scipy` and `numpy`.

---

## **License**
This project is licensed under the [MIT License](./LICENSE).
