# Optimization-project

## Instructions to run code

### Generating the files to be used by the Optimizer
Input files:
1. `deliveries.csv`: ball-by-ball IPL complete data
2. `IPLPLayerAuctionData.csv`: auction data
3. `unsold_players.csv`: unsold players in the 2022 auction

`player_performance.ipynb` calculates the player performance and merges it with auction data to produce 2 files: `final.csv` and `retained_players_final.csv`.

1. `final.csv`: Player name, Role, Amount, Player Origin, Average batting performance index, Average bowling performance index of players in the auction pool in 2022.
2. `retained_players_final.csv`: Player, Player Origin, Role, Average batting performance index, Average bowling performance index, Capped status for the players in the team of RCB 2021 (they can be retained)

### Running the Optimizer

1. Run `solution_general.py` for the list of players to be chosen for a team starting from scratch, assuming no players will be retained.
2. Run `solution_rcb.py` for the list of new players from the auction as well as the list of retained players to be chosen for RCB.

In both cases, a file called `player_names.txt` is generated containing the list of players to be chosen.
