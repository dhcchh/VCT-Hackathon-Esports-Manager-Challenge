# VCT International 2024 Data

## Overview
This folder contains CSV files related to the VCT International 2024 season.

## CSV Files
- **teams_vct_intl_2024.csv**: Contains details of all the teams participating in VCT International 2024.
- **leagues_vct_intl_2024.csv**: Contains details of all the leagues in the VCT International 2024.

### vct-intl-2024-teams.csv

| Column Name       | Description                                 | Data Type |
|-------------------|---------------------------------------------|-----------|
| `hq_location`     | Headquarters city of the team               | String    |
| `team_name`       | Official name of the team                   | String    |
| `abbreviation`    | Short form or abbreviation for the team     | String    |
| `owner`           | Name of the organisation or owner           | String    |
| `type`            | Type of the team. Partnered : Joined VCT-International through a partnership league, Ascended : Joined through VCT-Ascension, the final tournament in VCT Challengers| String    |
| `first_season`    | Year when the team joined the international league         | Integer   |
| `region`          | Geographic region where the team competes, AMER : Americas , APAC : Pacific, CN : China, EMEA : Eurpoe, Middle-East & Africa  | String |

### leagues_vct_intl_2024.csv

| Column Name       | Description                                 | Data Type |
|-------------------|---------------------------------------------|-----------|
| `tournament`     | Tournament name               | String    |
| `no_teams`       | Number of teams participating                   | String    |
| `abbreviation`    | Location(s) where the tournaments were being held     | String    |
| `start_date`           | First date of the tournament          | Datetime    |
| `end_date`            |Last date of the tournament| Datetime |
| `prize_pool_usd`    | Total prize pool of the tournament        | Integer   |
| `winner`          | Winner of the tournament, #1 placement overall | String|
|`runner_up` | RUnner up of the tournament, #2 placement overall |String |

