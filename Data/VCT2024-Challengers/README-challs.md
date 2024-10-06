
# VCT Challengers 2024 Data

## Overview
This folder contains CSV files related to the VCT Challengers 2024 Split 2 season.

## CSV Files

#### File Naming Convention:
- `challengers_split2_region.csv`: CSV files where "region" is replaced by specific tournament regions (e.g., Americas, China, EMEA, Pacific).

- **regions** included are **Americas, China, EMEA, Pacific**.

- Each **region** consists of multiple smaler **sub-regions**.

- `sub-regions.csv`: Contains the mapping of sub-regions to regions.
- `vct_challengers_americas.csv`: Player data from the Americas region.
- `vct_challengers_pacific.csv`: Player data from the Pacific region.
- `vct_challengers_china.csv`: Player data from the China region.
- `vct_challengers_emea.csv`: Player data from the EMEA region.

### Column Descriptions 

| Column Name       | Description                                                   | Data Type |
|-------------------|---------------------------------------------------------------|-----------|
| `country`         | The player's country of origin (e.g., Chile, Mexico).         | `string`  |
| `sub_region`      | The VALORANT sub region to which the player belongs (e.g. Brazil, Latin America South).                                                                             | `object`  |
| `language_1, language_2, language_3` | These are columns indicating the primary and additional languages spoken fluently by the player. If the player speaks only 1 language fluently, only lang_1 will have a value, if they speak 2 languages, lang_1 and lang_2 will have a value, if the player speaks 3 languages fluently, all 3 columns have a value. For example, player ign GLYPH speaks Filipino and English. language_1 will be Filipino, language_2 will be English, language_3 will have a null value.                                                                              | `string`  |
| `ign`             | The player's in-game name (IGN). (e.g. snw, Darker).          | `object`  |
| `team_role`       | The role of the player on the team (Flex, Entry, Smoker, Support, Anchor).                                                                            | `string`  |
| `igl`             |A boolean indicator of whether the player is the in-game leader (IGL). If the player is an IGL, then IGL is True, otherwise, it is False.                                |`bool`     |
| `standings`       | 	This represents the team's final placement in Stage 2 of the tournament series. The number indicates the specific rank, for example, 1 means 1st place, 2 means 2nd place, and so on. If the value is a range, such as 5th-6th, it means the team is tied with another team at that same placement.                                                                          | `string`  |
| `team_name_full`  |The full name of the team (e.g., SAGAZ, 9z Team).              | `object`  |
| `shorthand`       | The shorthand version of the team name (e.g., SGZ, 9ZG). If the team does not have a shorthand name, a null value would be given.                                        | `object`  |
| `agent_1, agent_2, agent_3`| These are columns indicating the top 3 most commonly used agents by the player in matches. If the player only plays one agent, only agent_1 will have a value, if the player plays 2 agents, only agent_1 and agent_2 has values, if a player plays 3 agents, all 3 columns have values. For example, Nate from Illicit Gaming plays Raze, followed by jett. Agent_1 will be Raze, Agent_2 will be Jett.                                                                               | `string`  |
| `maps`            | The number of maps the player has played in the tournament series.| `int64`|
| `k`               | The number of kills secured by the player throughout the entire tournament series.                                                                             | `int64`   |
| `d`               |The number of deaths the player experienced throughout the entire tournament series.                                                                             | `int64`   |
| `a`               | The number of assists secured by the player throughout the entire tournament series.                                                                             | `int64`   |
| `kd`              | 	The kill-to-death ratio for the player.                     | `float64` |
| `kda`             | The kill-death-assist ratio for the player.                   | `float64` |
| `acs_per_map`     | The average combat score per map in the tournament series.                                                                             | `float64` |
| `k_per_map`       | The average number of kills per map in the tournament series.                                                                             | `float64` |
| `d_per_map`       | The average number of deaths per map in the tournament series.                                                                             | `float64` |
| `a_per_map`       | The average number of assists per map in the tournament series.                                                                             | `float64` |

---

## Tournaments and Events

### Challengers Splits
- Contenders will have **up to 3 splits** a year in order to qualify for a spot in **Ascension**
- Teams that win earlier splits **qualifies** for later splits
- Top **1/2** teams of the **last split** would win them a spot in **Ascension** tournament
- Next few runners up are guaranteed a spot in the next split (if there is) 
- Winning the **Ascension** event would then promote them to the **international** leagues


## Regional Leagues
---
### Americas
- Total of **6** teams compete in **Ascension**. **Top 1** team promoted **VCT International**.

#### North America
- Top **8** teams from ***circuits** throughout 2024 advances to **playoffs**
- Players compete in **brackets** during **playoffs**
- **Top 2** teams from **playoffs** qualifies to play in **Ascension**

#### Latin America
- Consists of Latin America **North** and Latin America **South** sub-regions.
- Teams within each **sub-region** compete against each other to earn **circuit points**
- **Top 2** teams in **circuit points** from each **sub-region** advances to **Latin America Challengers**
- **Top 2** teams from **Latin America Challengers** advances to **Ascension**

#### Brazil
- Teams can qualify for **splits** by **circuit points**
- **10** teams from previous **split** and **relegations** play in brackets
- **Top 1** team from **split 2** advances to **Ascension**
- **Runner up** team in **circuit points** advances to **Ascension**
---

### Emea
- Total of **10** teams for **Ascension**. **Top 1** team promoted to **VCT International**.

#### North
- Teams can qualify for **splits** by **circuit points**
- Top **8** teams from previous **split** play in brackets.
- **Top 1** team advances to **Ascension**.
- **Runner up** team in **circuit points** advances to **Play-Ins**

#### Play-Ins
- **9** teams from other **sub-regions** play in brackets.
- **sub regions** include North, Spain, France, DACH, Turkey, East, MENA, Italy, Portugal.
- **Top 1** team advances to **Ascension**.

#### Turkey
- Teams can qualify for **splits** by **circuit points**
- **10 teams** from previous **split** and **relegations** play in brackets
- **Top 1** team advances to **Ascension**
- **Runner up** team in **circuit points** advances to **Play-Ins**

#### Mena
- Consists of **GCC & Iraq** and **Levant & North Africa sub-regions**
- Teams play in **circuits** in each **sub-region**
- **Top 2** teams from each **sub-region** compete in **MENA finals**
- **Top 1** team form **MENA finals** advances to **Ascension**
- **Runner up** team in **circuit points** advances to **Play-Ins**

#### Spain
- Teams can qualify for **splits** by **circuit points**
- **8 teams** from previous **split** play in brackets
- **Top 1** team advances to **Ascension**
- **Runner up** team in **circuit points** advances to **Play-Ins**

#### France, DACH, EAST, Italy, Portugal
- Teams earn points in **circuits** throughout the splits
- **Top 1** team from each sub-region advances to **Ascension**
- **Runner up** team in **circuit points** advances to **Play-Ins**
---

### Pacific
- Total of **10** teams for **Ascension**. **Top 1** team promoted to **VCT International**.

#### South Asia
- Teams can qualify for splits by **circuit points**
- Top **8** teams from **circuit** advances to **playoffs**
- **Top 1**  from **playoffs** advances to **Ascension**

#### Thailand
- **Top 4** from **circuit** advances to **Qualifiers**
- **Top 1** from **Qualifiers** advances to **Ascension**

#### Vietnam/Oceania/Malaysia & Singapore/Korea/Japan/Philippines/Indonesia
- Teams can qualify for splits by **circuit points**
- **8 teams** from previous split/promotion
- **Top 1** advances to **Ascension**

#### Hong Kong & Taiwan
- Teams can qualify for splits by **circuit points**
- **8 teams** from Open Qualifiers/Previous Split
- **Top 1** advances to **Ascension**
---

### China

#### Valorant China National Competition
- **8** teams selected from advancement group and **8** teams selected from breakout group compete to earn circuit points
- Advancement groups consists of winners and first runners up of the current and previous season national tournaments. The advancement group also consists of winners and 1st runners up of regional tournaments this year.
- Breakout groups consists of the 2nd and 3rd runners up of current and previous season national tournaments, as well as various smaller scale national tournaments of the current season.
- **Top 8** teams in circuit points advances to **Ascension**
---
