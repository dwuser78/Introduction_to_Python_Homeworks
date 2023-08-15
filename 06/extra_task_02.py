import sys

_SPLIT_TOKEN = ";"
_NUM_PARAM = 4

def collect_values(teams_table: dict, values: list):

    stats = {"all_games" : 0,
             "wins" : 1,
             "draws" : 2,
             "defeats" : 3,
             "total_points" : 4}

    team_stat_val: list = []
    teams: list = []
    points: list = []

    team_stat_val = [0] * len(stats)

    if len(values) != _NUM_PARAM:
        print("Error: Incorrect number of parameters")
        sys.exit(1)

    for i, value in enumerate(values):
        if (i % 2) == 0:
            if str(value).isalpha():
                teams.append(value.upper())
            else:
                print("Error: Incorrect string format. A string is expected.")
                sys.exit(1)
        else:
            if str(value).isdigit():
                points.append(int(value))
            else:
                print("Error: Incorrect string format. A number is expected.")
                sys.exit(1)

    for i in range(len(teams)):
        if teams[i] in teams_table.keys():
            teams_table[teams[i]][stats["all_games"]] +=1
            teams_table[teams[i]][stats["total_points"]] += points[i]

            if points[i - 1] < points[i]:
                teams_table[teams[i]][stats["wins"]] +=1
            elif points[i - 1] > points[i]:
                teams_table[teams[i]][stats["defeats"]] +=1
            else:
                teams_table[teams[i]][stats["draws"]] +=1
        else:
            team_stat_val[stats["all_games"]] += 1
            team_stat_val[stats["total_points"]] += points[i]

            if points[i - 1] < points[i]:
                team_stat_val[stats["wins"]] += 1
            elif points[i - 1] > points[i]:
                team_stat_val[stats["defeats"]] += 1
            else:
                team_stat_val[stats["draws"]] += 1

            teams_table[teams[i]] = team_stat_val

            team_stat_val.clear
            team_stat_val = [0] * len(stats)

def print_all_info(teams_table: dict):
    for key, values in teams_table.items():
        print(f"{key.title()}:", end="")

        for value in values:
            print(f"{value}", end=" ")

        print()


teams_table: dict = {}
tmp_str: str = input()

if not tmp_str.isdigit() or tmp_str == "":
    print("Error: Incorrect input")
    sys.exit(1)

num_str = int(tmp_str)

if num_str <= 0:
    print("Error: Incorrect number of rows")
    sys.exit(1)

for row_idx in range(num_str):
    values = input().split(_SPLIT_TOKEN)
    collect_values(teams_table, values)

print()
print_all_info(teams_table)