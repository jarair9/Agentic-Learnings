# Chapter 57: Multimodal Agents

Multimodal means using more than one type of input or output.

Examples:

- text
- images
- audio
- video
- PDFs
- spreadsheets
- screenshots

## 1. Why Multimodal Agents Matter

Users do not only work with text.

They may ask:

```text
Explain this diagram.
Read this screenshot.
Summarize this PDF.
Generate an image.
Transcribe this audio.
```

## 2. Image Agents

Image-capable agents can:

- describe screenshots
- inspect UI bugs
- read charts
- understand diagrams

Risks:

- OCR mistakes
- visual ambiguity
- privacy in screenshots

## 3. Audio Agents

Audio agents can:

- transcribe speech
- summarize meetings
- answer spoken questions

Risks:

- wrong transcription
- speaker confusion
- private conversations

## 4. File Agents

File agents can handle:

- PDFs
- Word documents
- CSV files
- spreadsheets

Good file agents extract text carefully and cite pages or rows.

## 5. Multimodal Safety

Before sending files to a model, ask:

- does the model need the whole file?
- does the file contain private data?
- can I extract only relevant parts?
- should I ask permission?

## Run

```powershell
python chapter_57_multimodal_agents/main.py
```

