# Optimization-project

## Instructions to run code:

Input files:
1. `deliveries.csv`: ball-by-ball IPL complete data
2. `IPLPLayerAuctionData.csv`: auction data
3. `unsold_players.csv`: unsold players in the 2022 auction

`player_performance.ipynb` calculates the player performance and merges it with auction data to produce 2 files: `final.csv` and `retained_players_final.csv`.

1. `final.csv`: Player name, Role, Amount, Player Origin, Average batting performance index, Average bowling performance index of players in the auction pool in 2022.
2. `retained_players_final.csv`: Player, Player Origin, Role, Average batting performance index, Average bowling performance index, Capped status for the players in the team of RCB 2021 (they can be retained)

