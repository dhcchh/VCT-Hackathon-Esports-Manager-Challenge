# VCT International 2024 Data

## Overview
This folder contains CSV files related to the VCT International 2024 season.

## CSV Files
- **teams_vct_intl_2024.csv**: Contains details of all the teams participating in VCT International 2024.
- **leagues_vct_intl_2024.csv**: Contains details of all the leagues in the VCT International 2024.

### vct-intl-2024-leagues.csv 
This data is from the VCT International Stage 2 of each region. We select this tournament for our pool of international players as it is the highest tier tournament where every player in the league had a chance to compete.
| Column Name       | Description                                                                 | Data Type   |
|-------------------|-----------------------------------------------------------------------------|-------------|
| **country**       | The player's country of origin (e.g., Taiwan, China).                       | `object`    |
| **valo_region**   | The VALORANT region to which the player belongs (e.g., CN for China).        | `object`    |
| **lang_1, lang_2, lang_3** | The primary and additional languages spoken by the player.          | `object`    |
| **ign**           | The player's in-game name (IGN).                                             | `object`    |
| **team_role**     | The role of the player on the team (e.g., Flex, Fragger, Smoker).            | `object`    |
| **igl**           | A boolean indicator of whether the player is the in-game leader (True/False).| `bool`      |
| **standings**     | The final standings of the team in Stage 2 of the tournament.                | `int64`     |
| **team_name_full**| The full name of the team (e.g., Wolves Esports).                           | `object`    |
| **shorthand**     | The shorthand version of the team name (e.g., Wolves).                      | `object`    |
| **agent_1, agent_2, agent_3** | The agents used by the player in matches.                      | `object`    |
| **maps**          | The number of maps the player has played.                                   | `int64`     |
| **k**             | The number of kills secured by the player.                                  | `int64`     |
| **d**             | The number of deaths the player experienced.                                | `int64`     |
| **a**             | The number of assists the player provided.                                  | `int64`     |
| **kd**            | The kill-to-death ratio for the player.                                     | `float64`   |
| **kda**           | The kill-death-assist ratio for the player.                                 | `float64`   |
| **acs_per_map**   | The average combat score per map.                                           | `float64`   |
| **k_per_map**     | The average number of kills per map.                                        | `float64`   |
| **d_per_map**     | The average number of deaths per map.                                       | `float64`   |
| **a_per_map**     | The average number of assists per map.

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

## Pro System Overview

### New Championship Points System
- Teams earn **1 point** for each win during League Stage games.
- Teams earn **3 points** for:
  - Winning regional Kickoff, Masters Madrid, Masters Shanghai, and Stage 1 Playoffs.
  - Winning their respective **Kickoff** event.

---

## Tournaments and Events

### Kickoff Event
- Four on-LAN Kickoff events, one in each international territory.
- Each Kickoff consists of **11 teams**.
- Teams earn **3 additional points** for winning their respective Kickoff event.
- **Top 2 teams** from each Kickoff qualify for **Masters Madrid**.

### Masters Events
- **Two Masters events** take place along the circuit:
  - **Masters 1 - Madrid**: March, Madrid, Spain.
    - Top 2 teams from each Kickoff event play for Championship Points.
  - **Masters 2 - Shanghai**: May, Shanghai, China.
    - Top 3 teams from each International League - Stage 1 play for Championship Points.
- Teams earn **3 points** for winning each Masters event.

---

## International Leagues

### Overview
- Two Stages of International Leagues along the circuit.
- Teams earn **1 point** for each win during League Stage games.
- Teams earn **3 additional points** for winning their respective International League Playoffs.
- Events will take place during **March-May** and **May-July**.

### Leagues and Locations
- **Americas League**: Played in Los Angeles, United States.
- **China League**: Played in Shanghai, China.
- **EMEA League**: Played in Berlin, Germany.
- **Pacific League**: Played in Seoul, South Korea.

---

### International League - Stage 1
- Four on-LAN leagues, one in each international territory.
- Each league consists of **11 partner teams**.
- **Top 3 teams** from each league qualify for **Masters Shanghai**.
- Teams earn **Championship Points** to qualify for **Champions 2024**.

### International League - Stage 2
- Four on-LAN leagues, one in each international territory.
- Each league consists of **11 partner teams**.
- **Top 3 teams** from each league qualify for **Champions**.
- Teams earn **Championship Points** to qualify for **Champions**.

---

## Champions
- Event takes place in **Seoul, South Korea**.
- Features **3 teams from each International League - Stage 2** and **1 team** from Championship Points.
- Teams compete for the title of World Champion.

### Slot Distribution
- **Americas**: 4 slots (3 teams from Stage 2 + 1 from Championship Points).
- **China**: 4 slots (3 teams from Stage 2 + 1 from Championship Points).
- **EMEA**: 4 slots (3 teams from Stage 2 + 1 from Championship Points).
- **Pacific**: 4 slots (3 teams from Stage 2 + 1 from Championship Points).

---
