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

file_path = "daily_discussion_april_12.txt"

# Get the chunks from the file
chunks = get_chunks_from_file(file_path)

# Get the users, comments, and users with multiple posts from the chunks
dic, users, users_with_multiple_posts = get_users_comments_from_chunks(chunks)

# Get the users who mentioned "cough", "cold", or "fever"
cough_mentions, cold_mentions, fever_mentions = get_mentions_with_cough_cold_fever(dic)

print(len(users))
print(len(users_with_multiple_posts))
print(cough_mentions)    