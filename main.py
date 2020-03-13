import sys
from include.get_user_commits import get_user_commits


def main():
    try:
        if (len(sys.argv) > 4):
            print("WARNING: Only three arguments needed: your_username, my_username, and my_password.")
        df = get_user_commits(sys.argv[1], sys.argv[2], sys.argv[3])
        print(df.to_string(index=False))
        print("\nTotal repositories:", len(df.index))
        print("Total commits:", df['Commits'].sum())
    except IndexError:
        print("ERROR: Check that there are exactly three arguments: your_username, my_username, and my_password.")
    except TypeError:
        print("ERROR: Check that the three arguments (your_username, my_username, and my_password) do not contain any typos.")

#-------------------------#

if __name__ == "__main__":
    main()
