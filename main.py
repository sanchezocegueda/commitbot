from config import *
import random, datetime, subprocess, time


def main():

    # Randomly selected number of commits to perform for the day
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)

    for i in range(num_commits):

        # Write contents to file
        with open(FILE_NAME, "a") as f:
            msg = f"{datetime.date.today()}: Commit {i+1}/{num_commits}." 

            subprocess.run(ECHO + [msg])

            f.write(msg + "\n")

        time.sleep(1)

        # git add            
        try:
            subprocess.run(GIT_ADD + [FILE_NAME], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Add failed: {e}, {e.stderr}")
            raise

        # git commit
        try:
            subprocess.run(GIT_COMMIT + [msg], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Commit failed: {e}")
            raise

    # git push
    try:
        subprocess.run(GIT_PUSH, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Push failed: {e}")
        raise


    return

if __name__ == '__main__':
    main()