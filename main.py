from config import *
import config, random, datetime, subprocess


def main():

    # Randomly selected number of commits to perform for the day
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)

    with open(FILE_NAME, "a") as f:
        for i in range(num_commits):
            msg = f"{datetime.datetime.now()}: Commit {i}/{num_commits}." 
            f.write(msg)
            
            subprocess.run(GIT_ADD, FILE_NAME)
            subprocess.run(GIT_COMMIT, msg)

    subprocess.run(GIT_PUSH)


    return

if __name__ == '__main__':
    main()