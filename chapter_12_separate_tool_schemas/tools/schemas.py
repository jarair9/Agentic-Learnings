# schemas.py contains the tool descriptions the model can see.
# Keep schemas as data. Do not put real tool logic here.

TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "explain_python_concept",
        "description": "Explain a Python concept in a beginner-friendly way.",
        "parameters": {
            "type": "object",
            "properties": {
                "concept": {
                    "type": "string",
                    "description": "The Python concept to explain.",
                }
            },
            "required": ["concept"],
            "additionalProperties": False,
        },
    }
]

