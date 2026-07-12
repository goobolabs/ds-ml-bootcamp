# Bonus – AI & Generative AI

> The last bonus guide showed you the math — vectors, matrices, gradients — underneath the models you've built. This guide zooms in on the branch of AI that made headlines everywhere, built on that same math: Generative AI, LLMs, and the tools built on top of them.

---

By now you have probably used ChatGPT, Gemini, or Claude yourself. This guide answers the question students ask most: **what is actually happening under the hood?**

---

## AI vs ML vs Deep Learning

These three terms get used interchangeably, but they are nested inside each other:

- **Artificial Intelligence (AI):** The broad goal of making machines act intelligently. Includes everything from a chess bot to a self-driving car.
- **Machine Learning (ML):** A subset of AI where machines learn patterns from data instead of following hardcoded rules. This is what you practiced in Lessons 4–6.
- **Deep Learning:** A subset of ML using neural networks, covered in the previous bonus guide.
- **Generative AI:** A subset of Deep Learning focused on *creating* new content — text, images, audio, code — instead of just predicting a label or number.

---

## What is Generative AI?

Everything you built in this bootcamp was **predictive**: given inputs, predict a price, a category, or a cluster. Generative AI flips this around — given a prompt, it **generates** new, original output that did not exist before.

- **Text generation:** ChatGPT, Claude, Gemini writing essays, code, or answers.
- **Image generation:** Midjourney, DALL-E, Stable Diffusion turning a text prompt into a picture.
- **Audio and video generation:** Tools that generate speech, music, or short video clips from a prompt.

---

## Large Language Models (LLMs)

An LLM is a massive Transformer-based neural network trained on huge amounts of text from the internet, books, and code. Its core skill is deceptively simple: **predict the next word**, over and over, given everything written so far.

Trained at a large enough scale, that simple skill produces models that can write, summarize, translate, and reason about problems — which is why LLMs like GPT, Claude, and Gemini feel so capable.

---

## Embeddings and Vector Databases

- **Embeddings:** A way of converting text (or images) into a list of numbers (a vector) that captures its *meaning*. Sentences with similar meaning end up with similar vectors, even if the words are completely different.
- **Vector Databases:** A specialized database (like Pinecone, Weaviate, or ChromaDB) built to store embeddings and quickly find the ones most similar to a new query — the same way a search engine finds relevant pages, but based on meaning instead of exact keywords.

---

## Retrieval-Augmented Generation (RAG)

LLMs only know what they were trained on, and they do not know your company's private documents or today's news. **RAG** solves this by combining two steps:

1. **Retrieve:** Search a vector database for the most relevant chunks of information related to the user's question.
2. **Generate:** Feed those chunks into the LLM along with the question, so it answers using real, up-to-date, specific information instead of guessing.

RAG is how most "chat with your documents" or company chatbot products work today.

---

## Fine-Tuning vs Prompting

There are two ways to make an LLM behave the way you want:

- **Prompting:** Just describe what you want in plain English inside your message ("Answer like a friendly teacher"). Fast, free, and usually enough.
- **Fine-Tuning:** Actually retraining the model further on your own examples so the behavior is baked in. Expensive, slower, and usually only needed for specialized, high-volume use cases.

Most real-world products rely almost entirely on good prompting (and RAG), not fine-tuning.

---

## AI Agents

An **AI Agent** is an LLM given the ability to take actions, not just generate text — searching the web, running code, calling APIs, or using tools — and to repeat that loop until a task is done, rather than answering in a single reply.

This bootcamp's traditional ML models predicted a single output. Agents chain many LLM calls and tool calls together to complete multi-step tasks, which is the direction most cutting-edge AI products are heading.

---

*Bonus guide — AI & Generative AI*

Proceed to [**Bonus – Career Path in ML**](05-career-path-in-ml.md) next to see which industry roles work with these tools day to day.

---
