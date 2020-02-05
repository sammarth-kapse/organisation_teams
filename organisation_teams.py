import json
from teams_info import get_teams_info
from developers_info import get_developers_info

organisation = "Test-webhook"
teams_info = get_teams_info(organisation)
print(teams_info)
with open("team_data" + '.json', 'w', encoding='utf-8') as f:
    json.dump(teams_info, f, ensure_ascii=False, indent=4)

developers_info = get_developers_info(organisation)
print(developers_info)
with open("developers_data" + '.json', 'w', encoding='utf-8') as f:
    json.dump(developers_info, f, ensure_ascii=False, indent=4)
