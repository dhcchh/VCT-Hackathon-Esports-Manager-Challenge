from data_analysis import load_and_merge_data, analyze_player_performance, analyze_team_performance, save_results

def main():
    # Step 1: Load and merge data
    merged_df = load_and_merge_data()

    # Step 2: Analyze player and team performance
    player_performance = analyze_player_performance(merged_df)
    team_performance = analyze_team_performance(merged_df)

    # Step 3: Save the results to CSV files
    save_results(player_performance, team_performance)

if __name__ == "__main__":
    main()