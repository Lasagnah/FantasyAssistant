import sys
from database import setup_database
from draft import draft_players
from prediction_method import display_prediction_results

if __name__ == "__main__":
    setup_database()
    draft_players()
