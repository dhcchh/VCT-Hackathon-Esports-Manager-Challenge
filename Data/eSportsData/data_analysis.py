import pandas as pd

# Define the function to load and merge datasets
def load_and_merge_data():
    # Load datasets from the ./Data/eSportsData/ folder
    leagues_df = pd.read_csv('./Data/eSportsData/leagues_cleaned.csv')
    mapping_data_df = pd.read_csv('./Data/eSportsData/mapping_data_cleaned.csv')
    players_df = pd.read_csv('./Data/eSportsData/players_cleaned.csv')
    teams_df = pd.read_csv('./Data/eSportsData/teams_cleaned.csv')
    tournaments_df = pd.read_csv('./Data/eSportsData/tournaments_cleaned.csv')

    # Merge mapping data with players (include first_name, last_name, and handle)
    merged_df = mapping_data_df.merge(players_df[['id', 'first_name', 'last_name', 'handle']], left_on='participantMapping.1', right_on='id', how='left')
    
    # Create fullName column in the format: first_name + 'in-game name' + last_name
    merged_df['fullName'] = merged_df['first_name'] + " '" + merged_df['handle'] + "' " + merged_df['last_name']
    
    # Merge with teams to get team names
    merged_df = merged_df.merge(teams_df[['id', 'name']], left_on='teamMapping.18', right_on='id', how='left')
    
    # Rename the column to teamName for clarity
    merged_df = merged_df.rename(columns={'name': 'teamName'})

    # Merge with tournaments to get tournament details
    merged_df = merged_df.merge(tournaments_df, left_on='tournamentId', right_on='id', how='left')

    # Clean data: handle missing values (you can modify this based on the needs)
    merged_df.dropna(inplace=True)

    # Add basic KDA metrics as placeholders (assuming K/D/A columns are available or calculable)
    merged_df['kills'] = merged_df['participantMapping.1'].apply(lambda x: x % 10)  # Dummy value
    merged_df['deaths'] = merged_df['participantMapping.1'].apply(lambda x: (x + 1) % 5)  # Dummy value
    merged_df['assists'] = merged_df['participantMapping.1'].apply(lambda x: (x + 2) % 3)  # Dummy value

    # Calculate KDA ratio
    merged_df['KDA_ratio'] = (merged_df['kills'] + merged_df['assists']) / merged_df['deaths']

    return merged_df

# Analyze player performance (including full player names in the new format)
def analyze_player_performance(merged_df):
    player_performance = merged_df.groupby(['participantMapping.1', 'fullName']).agg({
        'kills': 'sum',
        'deaths': 'sum',
        'assists': 'sum',
        'KDA_ratio': 'mean'
    }).reset_index()

    return player_performance

# Analyze team performance (using team names)
def analyze_team_performance(merged_df):
    team_performance = merged_df.groupby(['teamMapping.18', 'teamName']).agg({
        'kills': 'sum',
        'deaths': 'sum',
        'assists': 'sum',
        'KDA_ratio': 'mean'
    }).reset_index()

    return team_performance

# Save the analysis results
def save_results(player_performance, team_performance):
    player_performance.to_csv('./Data/eSportsData/player_performance.csv', index=False)
    team_performance.to_csv('./Data/eSportsData/team_performance.csv', index=False)
    print("Analysis results saved to ./Data/eSportsData/ folder.")