# VCT International 2024 Data

## Overview
This folder contains CSV files related to the VCT International 2024 season.

## CSV Files
- **vct-intl-2024-s2-players.csv** : Contains information about players participating in each region
- **teams_vct_intl_2024.csv**: Contains details of all the teams participating in VCT International 2024.
- **leagues_vct_intl_2024.csv**: Contains details of all the leagues in the VCT International 2024.

### vct-intl-2024-s2-players.csv 
This table below documents the vct-intl-2024-s2-players.csv file. It contains data about players of all the players participating in the VCT Stage 2 tournament series for each region. It provides an detailed explanation on what data each column containes and how it is interpreted.
We select this tournament series for our pool of international players as it is the highest tier tournament where every player in the league had a chance to compete.
| Column Name       | Description                                                                  | Data Type   |
|-------------------|----------------------------------------------------------------------------- |-------------|
| **country**       | The player's country of origin (e.g., Taiwan, China).                        | `string`    |
| **valo_region**   | The VALORANT region to which the player belongs (CN for Chinal, AMER for Americas, EMEA for Europe, Middle-East and Africa, PAC for Pacific).        | `object`    |
| **lang_1, lang_2, lang_3** | These are columns indicating the primary and additional languages spoken fluently by the player. If the player speaks only 1 language fluently, only lang_1 will have a value, if they speak 2 languages, lang_1 and lang_2 will have a value, if the player speaks 3 languages fluently, all 3 columns have a value. For example, PRX f0rsakeN speaks English and Indonesian, lang_1 will be Indonesian, lang_2 will be English and lang_3 will have a null value   | `string`    |
| **ign**           | The player's in-game name (IGN), e.g. f0rsakeN, Jingg, Derke, TenZ.                                             | `object`    |
| **team_role**     | The role of the player on the team (Flex, Entry, Smoker, Support, Anchor).            | `string`    |
| **igl**           | A boolean indicator of whether the player is the in-game leader (IGL). If the player is an IGL, then IGL is True, otherwise, it is False.| `bool`      |
| **standings** | This represents the team's final placement in Stage 2 of the tournament series. The number indicates the specific rank, for example, **1** means **1st place**, **2** means **2nd place**, and so on. If the value is a range, such as **5th-6th**, it means the team is tied with another team at that same placement.                | `string`     |
| **team_name_full**| The full name of the team (e.g., Paper Rex, Fnatic ).                                | `object`    |
| **shorthand**     | The shorthand version of the team name (e.g., PRX, FNC).                          | `object`    |
| **agent_1, agent_2, agent_3** | These are columns indicating the top 3 most commonly used agents by the player in matches. If the player only plays one agent, only agent_1 will have a value, if the player plays 2 agents, only agent_1 and agent_2 has values, if a player plays 3 agents, all 3 columns have values. For example, t3xture from Gen.G Esports plays Jett followed by Raze, agent_1 will be Jett, agent_2 will be Raze, agent_3 will be a null value                    | `string`    |
| **maps**          | The number of maps the player has played in the tournament series.                                    | `int64`     |
| **k**             | The number of kills secured by the player throughout the entire tournament series. | `int64`     |
| **d**             | The number of deaths the player experienced throughout the entire tournament series..  | `int64`     |
| **a**             | The number of assists secured by the player throughout the entire tournament series..    | `int64`     |
| **kd**            | The kill-to-death ratio for the player.                                      | `float64`   |
| **kda**           | The kill-death-assist ratio for the player.                                  | `float64`   |
| **acs_per_map**   | The average combat score per map in the tournament series.                                           | `float64`   |
| **k_per_map**     | The average number of kills per map in the tournament series.                                         | `float64`   |
| **d_per_map**     | The average number of deaths per map in the tournament series.                                        | `float64`   |
| **a_per_map**     | The average number of assists per map in the tournament series.                                       | `float64`   |

### vct-intl-2024-teams.csv

| Column Name       | Description                                 | Data Type |
|-------------------|---------------------------------------------|-----------|
| `hq_location`     | Headquarters city of the team               | String    |
| `team_name`       | Official name of the team                   | String    |
| `abbreviation`    | Short form or abbreviation for the team     | String    |
| `owner`           | Name of the organisation or owner           | String    |
| `type`            | Type of the team. Partnered : Joined VCT-International through a partnership agreement, Ascended : Joined through VCT-Ascension, the final tournament in VCT Challengers| String    |
| `first_season`    | Year when the team joined the international league         | Integer   |
| `region`          | Geographic region where the team competes, AMER : Americas - North & South America , APAC : Asia Pacific, CN : China, EMEA : Eurpoe, Middle-East & Africa  | String |

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
---
