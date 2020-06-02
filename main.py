import sys
from include.get_user_commits import get_user_commits


def main():
    """
    The main function that reads in two arguments (your_username and my_token)
    from the command line and calls get_user_commits() for your_username.
    Prints out all public, non-forked GitHub repositories belonging to your_username
    in a pandas dataframe, sorted according to the no. of commits to their
    respective default branch from your_username.
    
    Throws:
        UnboundLocalError: Exception if no arguments given to command line.
    """
    try:
        if (len(sys.argv) > 3):
            print("WARNING: Only two arguments needed: your_username and my_token.")
        
        if (len(sys.argv) == 2):
            df = get_user_commits(sys.argv[1])
        elif (len(sys.argv) == 3):
            df = get_user_commits(sys.argv[1], sys.argv[2])
        
        print(df.to_string(index=False))
        print("\nTotal repositories:", len(df.index))
        print("Total commits:", df['Commits'].sum())
        
    except UnboundLocalError:
        print("ERROR: Check that there is at least one argument: your_username (always required) and my_token (optional but recommended in case hourly API rate limit is exceeded).")

#-------------------------#

if __name__ == "__main__":
    main()
