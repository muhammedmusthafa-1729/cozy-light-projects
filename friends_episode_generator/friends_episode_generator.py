from numpy import *
import random


def open_episode(season, episode):
    import os
    # Insert the directory path in here
    path = 'F:\Series\Friends'
    # Extracting all the contents in the directory corresponding to path
    list_folders = os.listdir(path=path)
    path = path + "\\" + list_folders[season-1]
    list_files = os.listdir(path=path)
    # list_files = [f for f in os.listdir(path=path) if os.path.isfile(f)]
    path = path + "\\" + list_files[episode-1]
    os.startfile(path)


def get_watched_episodes_list(file_path = "F:\Computer Languages\Python Files\\friends_watched_episodes.txt"):

    with open(file=file_path, mode="r") as watched_episodes_file:
        watched_episodes_list = watched_episodes_file.readlines()
    watched_episodes_list = [(int(episode.strip().strip("()").split(",")[0]), int(episode.strip().strip("()").split(",")[1])) for episode in watched_episodes_list]

    return watched_episodes_list


def find_episode_to_watch():
    Seasons = [1,2,3,4,5,6,7,8,9,10]
    Episodes = [24,24,25,24,24,25,24,24,24,18]
    episodes_list = []
    for i in Seasons:
        for j in range(1,Episodes[i-1]+1):
            episodes_list.append((i, j))

    watched_episodes_list = get_watched_episodes_list()
    # print(watched_episodes_list)

    unwatched_episodes = [episode for episode in episodes_list if episode not in watched_episodes_list]

    print("unwatched_episodes", len(unwatched_episodes))
    print("watched_episodes", 236 - len(unwatched_episodes))
    season_episode_tuple = random.choice(unwatched_episodes)
    season, episode = season_episode_tuple
    print(f"Season {season}, Episode {episode}")
    open_episode(season=season, episode=episode)

    with open("F:\Computer Languages\Python Files\\friends_watched_episodes.txt", "a") as watched_episodes_file:
        watched_episodes_file.write(f"{season_episode_tuple}\n")

def play_last_watched_episode():
    watched_episodes_list = get_watched_episodes_list()
    open_episode(*watched_episodes_list[len(watched_episodes_list)-1])

# play_last_watched_episode()

# find_episode_to_watch()

def find_episode_to_watch_0():
    last_full_list = get_watched_episodes_list(file_path="F:\Computer Languages\Python Files\\friends_watched_episodes_0.txt")
    watched_episodes_list = get_watched_episodes_list()
    list_length = len(watched_episodes_list) + 10
    list_to_select = last_full_list[:list_length]
    # print(watched_episodes_list)

    unwatched_episodes = [episode for episode in list_to_select if episode not in watched_episodes_list]

    season_episode_tuple = random.choice(unwatched_episodes)
    season, episode = season_episode_tuple
    print(f"Season {season}, Episode {episode}")
    open_episode(season=season, episode=episode)

    with open("F:\Computer Languages\Python Files\\friends_watched_episodes.txt", "a") as watched_episodes_file:
        watched_episodes_file.write(f"{season_episode_tuple}\n")
    watched_episodes_list = get_watched_episodes_list()
    print("unwatched_episodes", 236 - len(watched_episodes_list))
    print("watched_episodes", len(watched_episodes_list))

# play_last_watched_episode()

find_episode_to_watch_0()

# open_episode(7, 4)
        
# watched_episodes_list = get_watched_episodes_list()
# print(watched_episodes_list, len(watched_episodes_list))
# s_s = [c[0] for c in watched_episodes_list]
# for i in range(1, 11):
#     print(i, s_s.count(i))

# counts = [s_s.count(i) for i in range(1, 11)]
# print(counts)
# for i in range(10):
#     subset = random.choices(counts, k=5)

#     print(sum(subset), sum(counts))
