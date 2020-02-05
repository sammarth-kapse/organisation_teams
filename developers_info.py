from helper_functions import *
from teams_info import get_team_members


def get_developers_info(organisation):
    url = BASE_URL + "/" + organisation + "/" + TEAMS

    developers_to_team_mapping = map_developer_to_teams_hierarchy(url, organisation)
    developers_info = []
    for key in developers_to_team_mapping:
        info = {DEVELOPER: key, TEAMS: developers_to_team_mapping[key]}
        developers_info.append(info)

    return developers_info


def map_developer_to_teams_hierarchy(url, organisation):
    teams_data = get_data_collection_from_github_api(url)
    developers_info_map = {}
    for team in teams_data:
        team_members = get_team_members(organisation, team[SLUG])
        for member in team_members:
            if member not in developers_info_map:
                developers_info_map[member] = [team[NAME]]
            else:
                developers_info_map[member].append(team[NAME])

    return developers_info_map
