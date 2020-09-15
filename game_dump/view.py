import json
import logging
from .data import RawGameData, RawEventData, NoMatchingGames, ApiError


logger = logging.getLogger()


class View(object):
    """
    The BaseView object provides base functionality for all Views.
    This class stores a set of game IDs, and displays game summary
    data for each one.

    For each game ID, this class:
    - creates an object to wrap the raw event data
    - creates an object to parse the raw data and create game summary data
    - displays the game summary data using subclass-specific method

    View classes. The View class creates a RawEventData class,
    gets the raw event data for the given game ID, and parses
    it for viewing. The parsing functions are common to all 
    View classes.
    """
    def __init__(self, options):
        """
        Get all of the game summary data here.

        Game data is stored in a dictionary - key is game ID,
        value is the game summary JSON object.
        """
        self.game_id = options.game_id

        # API data wrapper for game data
        try:
            gd = RawGameData(self.game_id)
            self.game_data = gd.game
        except NoMatchingGames as e:
            msg = f"No matching games found for game id {self.game_id}. Quitting..."
            logger.error(msg)
            print(msg)
            exit(1)
        except ApiError as e:
            msg = f"Error reaching /gameById API for game id {self.game_id}. Quitting..."
            logger.error(msg)
            print(msg)
            exit(1)

        # API data wrapper for event data
        try:
            self.ed = RawEventData(self.game_id)
        except NoMatchingGames as e:
            msg = f"No matching games found for game id {self.game_id}. Quitting..."
            error.log(msg)
            print(msg)
            exit(1)
        except ApiError as e:
            msg = f"Error reaching /events API for game id {self.game_id}. Quitting..."
            error.log(msg)
            print(msg)
            exit(1)

    def show(self):
        print("="*40)
        print("Blaseball Game Event Log")
        print("Game ID: %s"%(self.game_id))
        print("Season %d Day %d:"%(self.game_data['season']+1, self.game_data['day']+1))
        print("%s @ %s"%(
            self.game_data['awayTeamName'], 
            self.game_data['homeTeamName'],
        ))
        print("%s %d - %d %s"%(
            self.game_data['awayTeamNickname'], 
            self.game_data['awayScore'], 
            self.game_data['homeScore'],
            self.game_data['homeTeamNickname'],
        ))
        print("-"*40)
        for event in self.ed.events():
            print(json.dumps(event, indent=4))
            print("-"*40)
