def choose_multimodal_tool(file_name: str) -> str:
    extension = file_name.lower().split(".")[-1]

    if extension in {"png", "jpg", "jpeg"}:
        return "image_understanding_tool"

    if extension in {"mp3", "wav", "m4a"}:
        return "audio_transcription_tool"

    if extension in {"pdf"}:
        return "pdf_text_extraction_tool"

    if extension in {"csv", "xlsx"}:
        return "table_analysis_tool"

    return "unknown_file_tool"


def main() -> None:
    files = ["diagram.png", "lesson.pdf", "meeting.mp3", "scores.csv"]

    for file_name in files:
        print(file_name, "->", choose_multimodal_tool(file_name))


if __name__ == "__main__":
    main()

