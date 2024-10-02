

# VCT Game Changers 2024 Data

## Overview
This folder contains CSV files related to the VCT Game Changers

## CSV Files
- **gc_`p`.csv**: Contains details of all the teams participating in that particular **VCT Game Changers** `p (in lower case)` sub-region

- **sub-regions** included are **Pacific, North America, EMEA, Brazil, Latin America**

### gc_`p`.csv

| Column Name       | Description                                                   | Data Type |
|-------------------|---------------------------------------------------------------|-----------|
| `country`         | Country that player is from, `International` if not found     | String    |
| `sub_region`      | Sub region that tournament was played in                      | String    |
| `language_1/2/3`  | Languages spoken by player, `NaN` otherwise                   | String    |
| `ign`             | Player's in-game name                                         | String    |
| `team_role`       | Primary role played by the player                             | String    |
| `igl`             | Whether the player currently or was the leader of the team    | String    |
| `standings`       | Highest placement in tournament achieved by the player        | Integer   |
| `team_name_full`  | Full name of organisation the player is playing for           | String    |
| `shorthand`       | Shorthand name of organisation the player is playing for      | String    |
| `agent_1/2/3`     | Agents (in-game characters) played by the player, `NaN otherwise | String |
| `maps`            | Total number of maps played by the player in the the tournament | Integer |
| `k`               | Total number of kills made by the player                      | Integer   |
| `d`               | Total number of deaths of player                              | Integer   |
| `a`               | Total number of assists made by the player                    | Integer   |
| `kd`              | Total number of kills per deaths by player                    | Float     |
| `kda`             | Total number of kills and assists made per death by the player| Float     |
| `acs_per_map`     | Average combat score of player                                | Float     |
| `k_per_map`       | Total number of kills made by the player per map              | Float     |
| `d_per_map`       | Total number of deaths of the player per map                  | Float     |
| `a_per_map`       | Total number of assists made by the player per map            | Float     |

---
## Regional Leagues
---

### Pacific
- Consists of smaller regions such as **SEA, Japan, South Asia, Korea, Oceania**
- Data is curated from the **latest** series/split of smaller regions
- Top teams from each smaller region compete in **regional final**

---

### North America
- Data is curated from series 2 as it is the **latest** tournament with every team participating
- **Top 3** teams from each qualifier, **7 Runner ups** based on points

---

### Emea
- Data is curated from **series 1 & 2**. (**3rd** split **not** played yet)
- **Top 3** teams from each qualifier, **7 Runner ups** based on points

---

### Brazil
- Data is curated from **series 1 & 2**. (**3rd** split **not** played yet)
- **Top 3** teams from each qualifier, **7 Runner ups** based on points

---

### Latin America
- Consists of **North & South**, each with their own brackets
- Data is curated from **opening** games 
- **Top 1** team from North & South play in finals
---
