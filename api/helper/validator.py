from helper.jsonschema_validate import JSONSchemaValidator


class MovePieceValidator(JSONSchemaValidator):
    def __init__(self):
        self.schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "description": "Contract to move a chess piece.",
            "type": "object",
            "properties": {
                "player": {
                    "type": "string",
                    "enum": ["white", "black"]
                },
                "piece": {
                    "type": "string",
                    "enum": ["rook", "knight", "bishop",
                             "king", "queen", "pawn"]
                },
                "currentCoordinate": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "moveTo": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                }
            },
            "required": ["player", "piece", "currentCoordinate", "moveTo"]
        }
