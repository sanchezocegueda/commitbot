from config import *
import config, random, datetime, subprocess, time


def main():

    # Randomly selected number of commits to perform for the day
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)

    for i in range(num_commits):
        with open(FILE_NAME, "a") as f:
            msg = f"{datetime.date.today()}: Commit {i+1}/{num_commits}.\n" 
            subprocess.run(ECHO + [msg])
            f.write(msg)
            
            subprocess.run(GIT_ADD + [FILE_NAME])
            subprocess.run(GIT_COMMIT + [msg])
            time.sleep(2)

    subprocess.run(GIT_PUSH)


    return

if __name__ == '__main__':
    main()