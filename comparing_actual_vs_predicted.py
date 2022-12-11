import pandas as pd

cur_pred = "mult_penalty_beatavg.xlsx"
predicted = pd.ExcelFile(cur_pred)
actual = pd.ExcelFile("actual_lineups.xlsx")
match_diffs = pd.ExcelWriter("match_diffs.xlsx", engine='openpyxl')
count_diff = 0

for sheet in predicted.sheet_names:
    pred_lineup = predicted.parse(sheet, header=None)
    actual_lineup = actual.parse(sheet, header=None)
    pred_players = set(pred_lineup[0])
    actual_players = set(actual_lineup[0])
    new_played = pred_players.difference(actual_players)
    removed = actual_players.difference(pred_players)
    count_diff += len(new_played)
    diffs = {"Players Added": list(new_played), "Players Removed": list(removed)}
    df = pd.DataFrame(diffs)
    df.to_excel(match_diffs, sheet)
    print(new_played, removed)
print(count_diff/38)