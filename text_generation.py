from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("🧠 Mini GPT Text Generator")
print("Type 'quit' to exit\n")

while True:
    prompt = input("Enter your prompt: ")

    if prompt.lower() == "quit":
        print("Goodbye! 👋")
        break

    output = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        temperature=0.8
    )

    print("\nGenerated Text:\n")
    print(output[0]['generated_text'])
    print("-" * 60)
