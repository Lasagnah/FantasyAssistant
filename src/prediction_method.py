import numpy as np
from database import get_player_data


def calculate_team_state(team):
    """
    Calculate the state vector for a team based on their players' statistics.
    State includes: scoring potential, playmaking, defense, and efficiency.
    """
    if not team:
        return np.zeros(4)

    # Calculate team averages
    total_points = sum(player['points_per_game'] for player in team)
    total_assists = sum(player['assists_per_game'] for player in team)
    total_defense = sum(player['steals_per_game'] + player['blocks_per_game']
                        for player in team)

    # Calculate shooting efficiency
    fg_pcts = [float(player['fg_pct']) for player in team if player['fg_pct'] != '']
    avg_fg_pct = np.mean(fg_pcts) if fg_pcts else 0

    return np.array([
        total_points,  # Scoring potential
        total_assists,  # Playmaking
        total_defense,  # Defensive impact
        avg_fg_pct * 100  # Efficiency (converted to percentage)
    ])


def transition_probability(state1, state2):
    """
    Calculate transition probability between two states.
    Uses a simplified model based on statistical differences.
    """
    diff = np.abs(state1 - state2)
    # Normalize differences to get probability-like values
    return 1 / (1 + np.sum(diff) / 100)


def reward_function(state):
    """
    Calculate the reward value for a given state.
    Higher values indicate better team performance.
    """
    weights = np.array([1.0, 0.8, 0.6, 1.2])  # Weights for different aspects
    return np.sum(state * weights)


def value_iteration(states, gamma=0.9, theta=0.01, max_iterations=1000):
    """
    Perform value iteration to find optimal state values.

    Args:
        states: List of team states
        gamma: Discount factor
        theta: Convergence threshold
        max_iterations: Maximum number of iterations

    Returns:
        Dictionary of state values
    """
    V = {i: 0 for i in range(len(states))}

    for _ in range(max_iterations):
        delta = 0
        for i in range(len(states)):
            v = V[i]
            # Calculate new value based on transitions to all other states
            new_v = reward_function(states[i])
            for j in range(len(states)):
                prob = transition_probability(states[i], states[j])
                new_v += gamma * prob * V[j]

            V[i] = new_v
            delta = max(delta, abs(v - V[i]))

        if delta < theta:
            break

    return V


def predict_winner(teams):
    """
    Predict the winning team based on MDP analysis.

    Args:
        teams: List of teams, where each team is a list of players

    Returns:
        tuple: (winning_team_index, winning_probability, team_scores)
    """
    # Calculate state for each team
    team_states = [calculate_team_state(team) for team in teams]

    # Perform value iteration
    state_values = value_iteration(team_states)

    # Calculate winning probabilities
    total_value = sum(state_values.values())
    team_probabilities = [value / total_value for value in state_values.values()]

    # Calculate team scores based on state values
    team_scores = [reward_function(state) for state in team_states]

    # Find winning team
    winning_team = np.argmax(team_probabilities)
    winning_probability = team_probabilities[winning_team]

    return winning_team, winning_probability, team_scores


def display_prediction_results(teams):
    """
    Display detailed prediction results for all teams.

    Args:
        teams: List of teams, where each team is a list of players
    """
    winning_team, winning_prob, team_scores = predict_winner(teams)

    print("\nTeam Performance Prediction:")
    print("-" * 50)

    for i, (team, score) in enumerate(zip(teams, team_scores)):
        print(f"\nTeam {i + 1}:")
        print(f"Performance Score: {score:.2f}")

        # Display key statistics
        state = calculate_team_state(team)
        print(f"Key Metrics:")
        print(f"  - Total Scoring: {state[0]:.1f} points per game")
        print(f"  - Playmaking: {state[1]:.1f} assists per game")
        print(f"  - Defense Impact: {state[2]:.1f} stocks per game")
        print(f"  - Shooting Efficiency: {state[3]:.1f}%")

        if i == winning_team:
            print(f"\n*** Predicted Winner: Team {winning_team + 1} with {winning_prob * 100:.1f}% confidence ***")
