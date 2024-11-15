from database import get_player_data, setup_database
from prediction_method import display_prediction_results

def calculate_player_score(player):
    ppg = player['points_per_game']
    rpg = player['rebounds_per_game']
    apg = player['assists_per_game']
    return ppg + 1.2 * rpg + 1.5 * apg


def draft_players():
    available_players = get_player_data()

    while True:
        input_var = input("How many players would you like to play with? ")
        if input_var.isdigit():
            player_num = int(input_var)
            break
        else:
            print("An error occurred. Please enter a valid number.")

    teams = [[] for _ in range(player_num)]

    print("Welcome to the NBA Fantasy Draft!")
    round_count = 0
    while available_players and round_count < 10:
        print(f"\nRound {round_count + 1}:")
        order = range(player_num) if round_count % 2 == 0 else range(player_num - 1, -1, -1)

        for team in order:
            if available_players:
                print(f"\nTeam {team + 1}, it's your turn to draft.")

                sorted_players = sorted(available_players, key=calculate_player_score, reverse=True)

                print("Top 5 available players:")
                for i, player in enumerate(sorted_players[:5]):
                    score = calculate_player_score(player)
                    print(
                        f"{i + 1}. {player['name']} ({player['team']}) - PPG: {player['points_per_game']:.1f}, RPG: {player['rebounds_per_game']:.1f}, APG: {player['assists_per_game']:.1f}, Score: {score:.1f}")

                suggested_player = sorted_players[0]
                print(
                    f"\nSuggested pick: {suggested_player['name']} (Score: {calculate_player_score(suggested_player):.1f})")

                while True:
                    choice = input("Enter the number of the player you want to draft (or 's' to see more players): ")
                    if choice.lower() == 's':
                        print("\nAll available players:")
                        for i, player in enumerate(sorted_players):
                            score = calculate_player_score(player)
                            print(
                                f"{i + 1}. {player['name']} ({player['team']}) - PPG: {player['points_per_game']:.1f}, RPG: {player['rebounds_per_game']:.1f}, APG: {player['assists_per_game']:.1f}, Score: {score:.1f}")
                    elif choice.isdigit() and 0 < int(choice) <= len(available_players):
                        index = int(choice) - 1
                        drafted_player = sorted_players[index]
                        available_players.remove(drafted_player)
                        teams[team].append(drafted_player)
                        print(f"Team {team + 1} drafts {drafted_player['name']}.")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        round_count += 1

    print("\nDraft Results:")
    for i, team in enumerate(teams):
        print(f"\nTeam {i + 1}:")
        for player in team:
            print(
                f"  {player['name']} ({player['team']}) - PPG: {player['points_per_game']:.1f}, RPG: {player['rebounds_per_game']:.1f}, APG: {player['assists_per_game']:.1f}")

    display_prediction_results(teams)

if __name__ == "__main__":
    setup_database()  # Update the database before starting the draft
    draft_players()
