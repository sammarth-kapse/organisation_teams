from helper_functions import *


def get_teams_info(organisation):
    url = BASE_URL + "/" + organisation + "/" + TEAMS
    teams_data = get_data_collection_from_github_api(url)
    teams_info = []
    for data in teams_data:
        info = {TEAM: data[NAME], PARENT: get_parent(data[PARENT]),
                MEMBERS: get_team_members(organisation, data[SLUG])}
        teams_info.append(info)

    return teams_info


def get_team_members(organisation, team_slug):
    url = BASE_URL + "/" + organisation + "/" + TEAMS + "/" + team_slug + "/" + MEMBERS
    members_data = get_data_collection_from_github_api(url)
    members = []
    for data in members_data:
        info = {DEVELOPER: data[LOGIN]}
        members.append(info)

    return members


def get_parent(parent_data):
    if parent_data is not None:
        return parent_data[NAME]
    else:
        return None
