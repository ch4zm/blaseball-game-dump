# blaseball-game-dump

`game-dump` is a command line utility for dumping all events for a given game ID.

## Installing

Install using pip:

```text
pip install blaseball-game-dump
```

## Usage

The command line utility that is installed is called `game-dump`. 

Provide the game ID as the first and only argument:

```text
game-dump 3ae0ced8-a816-488a-b0be-0491d20a28d9
```

## Python API

If you prefer to use `game-dump` from Python instead of the command line,
you can use the Python API by importing and calling
the `game_dump()` command, passing in a list of
string containing whatever flags you would use on
the command line:

```python
from game_dump import game_dump

game_id = "fca6f5d2-e645-4354-985e-3080983eecb4"
output = game_dump([game_id, "--text"])
```

The function call returns the output that would be printed
to the console if the tool were run from the command line,
as a string. You can obtain the results as JSON by using 
`json.loads()` to load JSON from a string:

```python
from game_dump import game_dump
import json

game_id = "fca6f5d2-e645-4354-985e-3080983eecb4"
output = game_dump([game_id, "--json"])
```


## Using game-dump with game-finder

This tool works best with the [`game-finder`](https://github.com/ch4zm/blaseball-game-finder)
command line utility, which lets you find game IDs and filter
by various criteria:

```text
$ game-finder --season 4 --day 99 --team Tacos
3ae0ced8-a816-488a-b0be-0491d20a28d9

$ game-finder --season 4 --day 99 --team Tacos | xargs game-dump
========================================
Game ID: 3ae0ced8-a816-488a-b0be-0491d20a28d9
Unlimited Tacos @ Boston Flowers
Tacos 1 - 2 Flowers
----------------------------------------
{
    "id": 3589263,
    "perceived_at": "2020-08-29T07:00:03.393Z",
    "game_id": "3ae0ced8-a816-488a-b0be-0491d20a28d9",
    "event_type": "OUT",
    "event_index": 0,
    "inning": 0,
    "top_of_inning": true,
    "outs_before_play": 0,
    "batter_id": "27c68d7f-5e40-4afa-8b6f-9df47b79e7dd",
    "batter_team_id": "878c1bf6-0d21-4659-bfee-916c8314d69c",
    "pitcher_id": "24f6829e-7bb4-4e1e-8b59-a07514657e72",
    "pitcher_team_id": "3f8bbb15-61c0-4e3f-8e4a-907a5fb1565e",
    "home_score": 0,
    "away_score": 0,
    "home_strike_count": 3,
    "away_strike_count": 3,
    "batter_count": 0,
    "pitches": [
        "X"
    ],
    "total_strikes": 0,
    "total_balls": 0,
    "total_fouls": 0,
    "is_leadoff": true,
    "is_pinch_hit": false,
    "lineup_position": 0,
    "is_last_event_for_plate_appearance": true,
    "bases_hit": 0,
    "runs_batted_in": 0,
    "is_sacrifice_hit": false,
    "is_sacrifice_fly": false,
    "outs_on_play": 1,
    "is_double_play": false,
    "is_triple_play": false,
    "is_wild_pitch": false,
    "batted_ball_type": "GROUNDER",
    "is_bunt": false,
    "errors_on_play": 0,
    "batter_base_after_play": 0,
    "is_last_game_event": false,
    "event_text": [
        "Play ball!",
        "Top of 1, Unlimited Tacos batting.",
        "Basilio Mason batting for the Tacos.",
        "Basilio Mason hit a ground out to Margarito Nava."
    ],
    "additional_context": "",
    "season": 3,
    "day": 98,
    "parsing_error": false,
    "parsing_error_list": [],
    "fixed_error": false,
    "fixed_error_list": []
}
----------------------------------------
{
    "id": 3589264,
    "perceived_at": "2020-08-29T07:00:27.677Z",
    "game_id": "3ae0ced8-a816-488a-b0be-0491d20a28d9",
    "event_type": "STRIKEOUT",
    "event_index": 1,
    "inning": 0,
    "top_of_inning": true,
    "outs_before_play": 1,
    "batter_id": "63df8701-1871-4987-87d7-b55d4f1df2e9",
    "batter_team_id": "878c1bf6-0d21-4659-bfee-916c8314d69c",
    "pitcher_id": "24f6829e-7bb4-4e1e-8b59-a07514657e72",
    "pitcher_team_id": "3f8bbb15-61c0-4e3f-8e4a-907a5fb1565e",
    "home_score": 0,
    "away_score": 0,

    ...

```

See [blaseball-game-finder](https://github.com/ch4zm/blaseball-game-finder).

