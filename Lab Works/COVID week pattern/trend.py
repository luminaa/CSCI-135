import csv



# Get chunks from a file
def get_chunks_from_file(file_path):
    chunks = []
    chunk = []
    start = False 

    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            # Check if the line starts with "level"
            if line.startswith("level"):
                # If there's a previous chunk, add it to the list of chunks
                if chunk != []:
                    chunks.append(chunk)
                # Start a new chunk with this line
                chunk = [line.strip()]
                start = True

            # If a chunk has started, add the line to the current chunk
            elif start:
                # Check if the line is a deleted comment
                if line.strip() == "Comment deleted by user":
                    chunk = []
                    start = False
                    continue
                # Add the line to the current chunk
                chunk.append(line.strip())

    return chunks


# Get users, comments, and users with multiple posts from chunks
def get_users_comments_from_chunks(chunks):
    dic = {} 
    users_with_multiple_posts = set() 
    users = set() 

    for chunk in chunks:
        # Skip empty chunks
        if not chunk:
            continue

        # Extract the username of the user who wrote the chunk
        username = chunk[1]

        # If the user has already posted a comment before, add them to the set of users with multiple comments
        if username in dic:
            users_with_multiple_posts.add(username)

        # Add the user to the set of all users who posted comments
        users.add(username)

        # Extract the content of the chunk
        i = 5
        text = ""

        while i < len(chunk) and not chunk[i].startswith('Reply'):
            text += chunk[i]
            i += 1

        # Add the user's comment to the dictionary of comments
        if username not in dic:
            dic[username] = []
        dic[username].append(text)

    return dic, users, users_with_multiple_posts


# Get users who mentioned "cough", "cold", or "fever"
def get_mentions_with_cough_cold_fever(dic):
    cough_mentions = []
    cold_mentions = []
    fever_mentions = []

    for user, comments in dic.items():
        for comment in comments:
            # If the comment mentions the words "cough", "cold", or "fever", add the user and their comment to the list of mentions
            if "cough" in comment:
                cough_mentions.append([user, comment])
            if "cold" in comment:
                cold_mentions.append([user, comment])
            if "fever" in comment:
                fever_mentions.append([user, comment])

    return cough_mentions, cold_mentions, fever_mentions


# Get daily percentage of posts that mention cough, cold, and fever
def get_daily_mention_percentages(daily_posts, daily_cough_posts, daily_cold_posts, daily_fever_posts):
    daily_cough_percentage = []
    daily_cold_percentage = []
    daily_fever_percentage = []

    for i in range(len(daily_posts)):
        daily_cough_percentage.append(round(daily_cough_posts[i] / daily_posts[i] * 100, 3))
        daily_cold_percentage.append(round(daily_cold_posts[i] / daily_posts[i] * 100, 3))
        daily_fever_percentage.append(round(daily_fever_posts[i] / daily_posts[i] * 100, 3))

    return daily_cough_percentage, daily_cold_percentage, daily_fever_percentage


def write_daily_outputs_to_csv(daily_posts, daily_cough_posts, daily_cold_posts, daily_fever_posts, daily_cough_percentage, daily_cold_percentage, daily_fever_percentage):
    with open('daily_outputs.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row with the days
        writer.writerow(['', 'April 12', 'April 13', 'April 14', 'April 15', 'April 16', 'April 17', 'April 18'])

        # Write the daily counts for posts and mentions
        writer.writerow(['Total Posts'] + daily_posts)
        writer.writerow(['Cough Mentions'] + daily_cough_posts)
        writer.writerow(['Cold Mentions'] + daily_cold_posts)
        writer.writerow(['Fever Mentions'] + daily_fever_posts)

        # Write the daily percentages for posts that mention cough, cold, and fever
        writer.writerow(['Cough Percentage'] + daily_cough_percentage)
        writer.writerow(['Cold Percentage'] + daily_cold_percentage)
        writer.writerow(['Fever Percentage'] + daily_fever_percentage)



base_path = "daily_discussion_april_"
file_extension = ".txt"

daily_posts = []
daily_cough_posts = []
daily_cold_posts = []
daily_fever_posts = []

# Loop through the days and get the daily posts and mentions
for day in range(12, 19):
    file_path = base_path + str(day) + file_extension
    chunks = get_chunks_from_file(file_path)
    dic, users, users_with_multiple_posts = get_users_comments_from_chunks(chunks)
    cough_mentions, cold_mentions, fever_mentions = get_mentions_with_cough_cold_fever(dic)

    # Append the daily counts to the corresponding lists
    daily_posts.append(len(chunks))
    daily_cough_posts.append(len(cough_mentions))
    daily_cold_posts.append(len(cold_mentions))
    daily_fever_posts.append(len(fever_mentions))

daily_cough_percentage, daily_cold_percentage, daily_fever_percentage = get_daily_mention_percentages(daily_posts, daily_cough_posts, daily_cold_posts, daily_fever_posts)
write_daily_outputs_to_csv(daily_posts, daily_cough_posts, daily_cold_posts, daily_fever_posts, daily_cough_percentage, daily_cold_percentage, daily_fever_percentage)
