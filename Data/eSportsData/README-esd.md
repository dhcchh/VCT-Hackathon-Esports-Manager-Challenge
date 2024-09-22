## Key Column Information

| File                     | Column Name        | Description                                                   |
|--------------------------|--------------------|---------------------------------------------------------------|
| **leagues_cleaned.csv**   | `league_id`        | Unique identifier for each league.                            |
|                          | `region`           | Geographic region the league represents.                      |
|                          | `name`             | Official name of the league.                                  |
|                          | `slug`             | URL-friendly version of the league's name.                    |
|                          | `dark_logo_url`    | URL for the league’s dark logo.                               |
|                          | `light_logo_url`   | URL for the league’s light logo.                              |
| **mapping_data_cleaned.csv** | `platformGameId`   | Platform’s unique game identifier.                            |
|                          | `esportsGameId`    | Corresponding esports game identifier.                        |
|                          | `tournamentId`     | ID of the tournament the game is part of.                     |
|                          | `teamMapping`      | Mapping of platform team IDs to esports team IDs.             |
|                          | `participantMapping`| Mapping of platform player IDs to esports player IDs.         |
| **players_cleaned.csv**   | `id`               | Unique identifier for each player.                            |
|                          | `handle`           | In-game handle or username of the player.                     |
|                          | `first_name`       | Player’s real first name (if available).                      |
|                          | `last_name`        | Player’s real last name (if available).                       |
|                          | `status`           | Current status of the player (e.g., active, inactive).        |
|                          | `home_team_id`     | ID of the team the player is associated with.                 |
| **teams_cleaned.csv**     | `id`               | Unique identifier for each team.                              |
|                          | `name`             | Official name of the team.                                    |
|                          | `status`           | Current status of the team (e.g., active, inactive).          |
|                          | `league_id`        | ID of the league the team is associated with.                 |
| **tournaments_cleaned.csv**| `id`               | Unique identifier for each tournament.                        |
|                          | `name`             | Official name of the tournament.                              |
|                          | `status`           | Current status of the tournament (e.g., ongoing, completed).   |
|                          | `league_id`        | ID of the league the tournament is part of.                   |
|                          | `time_zone`        | Time zone in which the tournament is held.                    |
