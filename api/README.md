# Chess API

## Routes

|verb|route|description|
|-|-|-|
|POST|/game|Create new game|
|GET|/game/{gameId}|Return all pieces positions|
|PATCH|/game/{gameId}|Move a chess piece. [body](./helper/validator.py)|
