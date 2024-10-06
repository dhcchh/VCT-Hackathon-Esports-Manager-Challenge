# Evaluation of Free LLM Models for VALORANT Digital Assistant

The VCT project involves building a digital assistant powered by large language models (LLMs) to assist with explaining the gameplay, mechanics, and strategies of the game **VALORANT**. The following document compares several free-to-use LLM models to help decide which one best fits the needs of this project. The model should be capable of providing text-based responses, answering user questions, and handling domain-specific content related to esports and games.

## LLMs Evaluated

The following LLMs are freely available and have been taken into consideration for this project:

### 1. GPT-Neo (EleutherAI)

- **Description**: GPT-Neo is an open-source implementation of a GPT-like language model developed by EleutherAI. It is a popular alternative to OpenAI's GPT models and supports text generation based on large amounts of internet text data.
  
- **Key Features**:
  - **Model Sizes**: Available in two versions: 1.3 billion and 2.7 billion parameters.
  - **Training**: Pretrained on diverse text corpora from various domains, making it versatile for general use and adaptable for domain-specific tasks (like esports).
  - **Performance**: Generates fluent and coherent responses but may require fine-tuning for highly specialized or niche content like VALORANT strategies or agent mechanics.
  - **License**: Apache 2.0 (Free for commercial and non-commercial use).
  
- **Why Consider for VALORANT?**:
  - GPT-Neo is robust and can handle large amounts of context, making it suitable for providing detailed game mechanics explanations or answering in-game queries.
  - It can be fine-tuned further to understand VALORANT-specific terminology and gameplay.
  
- **Challenges**:
  - While it handles general text well, the absence of game-specific training means it might struggle with very detailed esports or VALORANT-specific questions without fine-tuning.

- **Link**: [GPT-Neo on Hugging Face](https://huggingface.co/EleutherAI/gpt-neo-2.7B)

---

### 2. GPT-J (EleutherAI)

- **Description**: GPT-J is another open-source GPT-like model developed by EleutherAI. It is smaller than GPT-3 and aims to balance performance and computational efficiency, making it accessible for projects with fewer computational resources.

- **Key Features**:
  - **Model Size**: 6 billion parameters.
  - **Training**: Similar to GPT-Neo, it is pretrained on a wide range of text data, offering solid general-purpose text generation.
  - **Performance**: GPT-J performs well for both short-form and long-form text generation, making it a versatile model for generating explanations, strategies, or game-related dialogue.
  - **License**: Apache 2.0 (Free to use).
  
- **Why Consider for VALORANT?**:
  - GPT-J offers more parameters than GPT-Neo, making it a stronger model for generating coherent and contextually rich answers to more complex questions about the game.
  - Its efficiency and ability to handle general text generation tasks make it suitable for a range of VALORANT topics, from game mechanics to esports tournaments.
  
- **Challenges**:
  - It still requires some fine-tuning to specialize in VALORANT-specific contexts, though it is versatile for general text-based applications.
  
- **Link**: [GPT-J on Hugging Face](https://huggingface.co/EleutherAI/gpt-j-6B)

---

### 3. DistilGPT-2

- **Description**: DistilGPT-2 is a lightweight, distilled version of OpenAI's GPT-2. It's faster and smaller, making it ideal for projects with limited computational resources or for faster deployment.

- **Key Features**:
  - **Model Size**: 124 million parameters (about 60% smaller and faster than GPT-2).
  - **Training**: Pretrained on a similar text corpus to GPT-2, but distilled for efficiency. It’s optimized for generating coherent text responses without heavy computational demand.
  - **Performance**: While smaller, it can still generate decent quality text. However, it lacks the depth and nuance of larger models like GPT-J or GPT-Neo.
  - **License**: MIT License (Free to use).
  
- **Why Consider for VALORANT?**:
  - If your goal is quick responses and low-latency text generation, DistilGPT-2 can handle basic conversations about the game.
  - Suitable for simpler or less resource-intensive tasks, such as basic game explanations or answering straightforward questions.

- **Challenges**:
  - Its smaller size means it may struggle with more complex or detailed VALORANT-specific queries.
  - Limited ability to provide deep insights or handle lengthy responses without losing coherence.
  
- **Link**: [DistilGPT-2 on Hugging Face](https://huggingface.co/distilgpt2)

---

### 4. Flan-T5 (Google)

- **Description**: Flan-T5 is a powerful, instruction-tuned model developed by Google that excels at generating responses for task-based requests. It's fine-tuned on instruction-based datasets, making it great for handling complex instructions or detailed requests.

- **Key Features**:
  - **Model Sizes**: Available in various sizes (Small, Base, Large, XL, XXL).
  - **Training**: Tuned specifically for tasks involving instructions or multiple-step responses, making it ideal for assisting users with detailed or procedural queries.
  - **Performance**: Flan-T5 excels at understanding nuanced instructions and generating precise responses, which could make it ideal for explaining game mechanics, agent strategies, and advanced techniques in VALORANT.
  - **License**: Apache 2.0 (Free to use).

- **Why Consider for VALORANT?**:
  - **Instruction-tuning** makes Flan-T5 great for handling specific instructions (e.g., "Explain how to use Jett's abilities in a 1v1 scenario").
  - Works well for detailed game breakdowns, providing step-by-step guidance and explanations.
  
- **Challenges**:
  - May require additional fine-tuning for better domain-specific knowledge of VALORANT, but its instruction-following nature makes it a strong candidate.
  
- **Link**: [Flan-T5 on Hugging Face](https://huggingface.co/google/flan-t5-large)

---

## Comparison Table

| Model             | Parameters        | Strengths                                      | Challenges                                    | License     |
|-------------------|-------------------|------------------------------------------------|----------------------------------------------|----------------------|
| GPT-Neo           | 1.3B/2.7B         | General-purpose text generation                | Requires fine-tuning for domain-specific tasks |  Apache 2.0   |
          
| GPT-J             | 6B                | General-purpose, balanced performance          | Requires fine-tuning for specialized content |  Apache 2.0   |
| DistilGPT-2       | 124M              | Lightweight, fast text generation              | Limited depth and complexity                 |  MIT          |
| Flan-T5           | Small - XXL       | Excellent for instruction-following tasks      | Needs domain-specific fine-tuning            | Apache 2.0   |

---

## Conclusion

For building a **VALORANT digital assistant** in Singapore, the following model recommendations can be made:

- **For General-Purpose Use**: 
    - **GPT-Neo** and **GPT-J** are strong general-purpose models. They are both open-source and can handle a wide range of tasks with good text generation capabilities. If you're focusing on fluency, coherence, and general knowledge of the game, these models are great starting points.
  
- **For Fast and Lightweight Deployment**:
  - **DistilGPT-2** is your go-to option for low-resource or fast response systems. Although it sacrifices some depth, it is sufficient for handling simpler, quick-response tasks, such as explaining basic game mechanics or answering casual queries.

- **For Instruction-Tuned Applications**:
  - **Flan-T5** is excellent for more structured responses and tasks that require following specific instructions. It's ideal for explaining complex in-game scenarios, providing step-by-step guides for VALORANT agents, or advanced mechanics.

### Recommended Path Forward

For the **VALORANT digital assistant** project:
- If you require deep game-specific analysis, consider **GPT-J** for its balance of size and efficiency.
- For specific, instruction-based responses (e.g., explaining strategies in VALORANT), **Flan-T5** is highly recommended.

Additionally, some models like **GPT-Neo** and **GPT-J** can be **fine-tuned** on domain-specific data (such as VALORANT esports data) to improve their ability to answer detailed, game-related queries accurately.

## Resources and Links

- [GPT-Neo on Hugging Face](https://huggingface.co/EleutherAI/gpt-neo-2.7B)
- [GPT-J on Hugging Face](https://huggingface.co/EleutherAI/gpt-j-6B)
- [DistilGPT-2 on Hugging Face](https://huggingface.co/distilgpt2)
- [Flan-T5 on Hugging Face](https://huggingface.co/google/flan-t5-large)

---

## License Information

All models mentioned are free to use but may have different licenses:
- **GPT-Neo & GPT-J**: Apache 2.0 (permissive for commercial and non-commercial use)
- **DistilGPT-2**: MIT License (highly permissive, not much of an issue to use)
- **Flan-T5**: Apache 2.0 (permissive for commercial and non-commercial use)
