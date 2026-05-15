TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "explain_python",
        "description": "Explain a Python concept simply.",
        "parameters": {
            "type": "object",
            "properties": {
                "concept": {
                    "type": "string",
                    "description": "The concept to explain.",
                }
            },
            "required": ["concept"],
            "additionalProperties": False,
        },
    }
]

