import sys
from include.get_user_commits import get_user_commits


def main():
    """
    The main function that reads in three arguments (your_username, my_username, and my_password)
    from the command line and calls get_user_commits() for your_username. Prints out all public,
    non-forked GitHub repositories belonging to your_username in a pandas dataframe, sorted according
    to the no. of commits to their respective default branch from your_username.
    
    Throws:
        IndexError: Exception if <3 arguments given to command line.
    """
    try:
        if (len(sys.argv) > 4):
            print("WARNING: Only three arguments needed: your_username, my_username, and my_password.")
        df = get_user_commits(sys.argv[1], sys.argv[2], sys.argv[3])
        print(df.to_string(index=False))
        print("\nTotal repositories:", len(df.index))
        print("Total commits:", df['Commits'].sum())
    except IndexError:
        print("ERROR: Check that there are exactly three arguments: your_username, my_username, and my_password.")

#-------------------------#

if __name__ == "__main__":
    main()
