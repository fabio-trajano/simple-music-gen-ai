from musicgen.generator import generate_music

def interactive_prompt():
    """Ask the user for a text prompt to generate music."""
    print("Welcome to the AI Music Generator!")
    prompt = input("Enter your music description (e.g., 'futuristic classic music'): ")
    output_file = input("Enter output file name (default: my_music): ") or "musicgen"
    generate_music(prompt, output_file)

if __name__ == "__main__":
    interactive_prompt()
