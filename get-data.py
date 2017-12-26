from draftkings import DraftKingsClient, Sport

print(DraftKingsClient.get_contests(sport=Sport.nba))