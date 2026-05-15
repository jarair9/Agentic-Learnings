TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "read_text_file",
        "description": "Read a text file from the allowed learning folder.",
        "parameters": {
            "type": "object",
            "properties": {
                "relative_path": {
                    "type": "string",
                    "description": "A relative file path such as agent_notes.txt.",
                }
            },
            "required": ["relative_path"],
            "additionalProperties": False,
        },
    }
]

