TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "read_note",
        "description": "Read a safe note file from the knowledge folder.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The note filename, such as agent_loops.txt.",
                }
            },
            "required": ["filename"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "explain_python",
        "description": "Get a simple explanation of a Python concept.",
        "parameters": {
            "type": "object",
            "properties": {
                "concept": {
                    "type": "string",
                    "description": "A Python concept such as function, loop, list, or dictionary.",
                }
            },
            "required": ["concept"],
            "additionalProperties": False,
        },
    },
]

