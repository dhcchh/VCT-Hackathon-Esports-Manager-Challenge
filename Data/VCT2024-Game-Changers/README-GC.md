
# VCT Game Changers 2024 Data

## Overview
This folder contains CSV files related to the VCT Game Changers.

## CSV Files
- Note that for the `Americas` region, it is split into various **sub-regions** such as Brazil, North America, Latin America.
- `gc_brazil.csv`: Contains information about players participating from `Brazil` sub-region
- `gc_emea.csv`: Contains information about players participating from `EMEA` region
- `gc_latam.csv`: Contains information about players participating from `Latin America` sub-region
- `gc_na.csv`: Contains information about players participating from `North America` sub-region
- `gc_pacific.csv`: Contains information about players participating from `Pacific` region

### Column Descriptions 
This table below documents the `gc_subregion/region.csv` file. It contains data about players of all the players participating in the various Game_changers tournament series for each region. It provides an detailed explanation on what data each column containes and how it is interpreted. We select these tournament series for our pool of sub-regional/regional players as they are the highest tier tournaments where most players in their sub-regions/regions had a chance to compete.

| Column Name       | Description                                                   | Data Type |
|-------------------|---------------------------------------------------------------|-----------|
| `country`         | The player's country of origin (e.g., Canada, Mexico).        | `string`  |
| `language_1, language_2, language_3` | These are columns indicating the primary and additional languages spoken fluently by the player. If the player speaks only 1 language fluently, only lang_1 will have a value, if they speak 2 languages, lang_1 and lang_2 will have a value, if the player speaks 3 languages fluently, all 3 columns have a value. For example, player ign 3DWN speaks English and French. language_1 will be English, language_2 will be French, language_3 will have a null value.      | `string`  |
| `ign`             | The player's in-game name (IGN). (e.g. Ache, Aebix).          | `object`  |
| `team_role`       | The role of the player on the team (Flex, Entry, Smoker, Support, Anchor).                                                                            | `string`  |
| `igl`             |A boolean indicator of whether the player is the in-game leader (IGL). If the player is an IGL, then IGL is True, otherwise, it is False.                                |`bool`     |
| `standings`       | 	This represents the team's final placement in Stage 2 of the tournament series. The number indicates the specific rank, for example, 1 means 1st place, 2 means 2nd place, and so on. If the value is a range, such as 5th-6th, it means the team is tied with another team at that same placement.                                                                          | `string`  |
| `team_name_full`  |The full name of the team (e.g., BOBA,   Gang Gang).           | `object`  |
| `shorthand`       | The shorthand version of the team name (e.g., BOBA, GANG). If the team does not have a shorthand name, a null value would be given.                                      | `object`  |
| `agent_1, agent_2, agent_3`| These are columns indicating the top 3 most commonly used agents by the player in matches. If the player only plays one agent, only agent_1 will have a value, if the player plays 2 agents, only agent_1 and agent_2 has values, if a player plays 3 agents, all 3 columns have values. For example, Angela from Invincible gc plays Raze, followed by jett. Agent_1 will be Raze, Agent_2 will be Jett.                                                                               | `string`  |
| `maps`            | The number of maps the player has played in the tournament series.| `int64`|
| `k`               | The number of kills secured by the player throughout the entire tournament series.                                                                             | `int64`   |
| `d`               |The number of deaths the player experienced throughout the entire tournament series.                                                                             | `int64`   |
| `a`               | The number of assists secured by the player throughout the entire tournament series.                                                                             | `int64`   |
| `kd`              | 	The kill-to-death ratio for the player.                     | `float64`     |
| `kda`             | The kill-death-assist ratio for the player.                   | `float64`     |
| `acs_per_map`     | The average combat score per map in the tournament series.                                                                             | `float64`     |
| `k_per_map`       | The average number of kills per map in the tournament series.                                                                             | `float64`     |
| `d_per_map`       | The average number of deaths per map in the tournament series.                                                                             | `float64`     |
| `a_per_map`       | The average number of assists per map in the tournament series.                                                                             | `float64`     |

---
## Regional Leagues
---

### Pacific
- Consists of smaller regions such as **SEA, Japan, South Asia, Korea, Oceania**.
- Data is curated from **SEA Stage 2**, **Japan Split 2**, **South Asia Split 2**, **Korea Stage 2**, **Oceania Stage 2**.
- **Top 3** from **SEA Stage 2** qualifies for **regional final**.
- **Top 2** form **Japan Split 2** qualifies for **regional final**.
- **Top 1** from **South Asia Split 2** qualifies for **regional final**.
- **Top 1** from **Korea Stage 2** qualifies for **regional final**.
- **Top 1** from **Oceania Stage 2** qualifies for **regional final**.
- **8 teams** competing in **regional final**.
- **Top 2** teams in **regional final** qualifies for **Championships**.
---

### North America
- Teams from previous **series** qualify for next **series**.
- Each **series** has 3 **Open Qualifiers**.
- In the **last series**, **Top 1** from each **Open Qualifier** and 5 **Runner ups** from **circuits** compete in brackets.
- **Top 1** from **last series** qualifies for **Championships**.
- Data is curated from **series 2 (Including the 3 Open Qualifiers)** as it is the **latest** tournament with **all games** played. Note that the **last series** is **series 3**.

---

### Emea
- Each **Sub region** has **circuits** to qualify for **Contenders**
- **Top 8** Teams from previous **stage** and **Top 2** teams from **Contenders** qualify for next **stage**
- **Top 1** team from **last stage** qualifies for **Championships**
- Data is curated from **Stage 1 & 2** as it is the **latest** tournament with **all games** played. Note that the **last stage** is **stage 3**.

---

### Brazil
- Total of **3 series** for teams to earn circuit points.
- **Top 2** teams from previous **series** and **6** Runner ups in circuit points earns more **circuit points**.
- **Top 1** team from brazil in **circuit points** qualifies for **Championships**.
- Data is curated from **series 1 & 2** as it is the **latest** tournament with **all games** played. Note that **last series** is **series 3**.

---

### Latin America
- Consists of **North** & **South** sub regions, each with their own brackets
- Data is curated from the opening games because they provide a balanced sample size—neither including too many irrelevant teams nor too few to be unrepresentative of the tournament. This ensures that the data is reflective of the overall competition.
- **Top 5** teams from **opening games** and **Top 1** team from **opening promotion** compete within each **sub region**
- **Top 1** team from both **sub regions** play in **Latin America finals**
- **Top 1** team from **Latin America finals** qualifies for **Championships**
---
