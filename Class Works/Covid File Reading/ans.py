chunks = [] # empty list to store discussion chunks
chunk = [] # an empty discussion chunk
start = False # a flag to indicate if a chunk has started

with open("daily_discussion_april_12.txt", mode="r", encoding="utf-8") as file:
    for line in file:

        # If the line starts with "level" and no chunk has started yet
        if line.startswith("level") and not start:  
            # If there's a previous chunk, add it to the list of chunks
            if chunk:
                chunks.append(chunk)
            # Start a new chunk with this line
            chunk.append(line.strip())
            start = True

        # If the line starts with "Reply" and a chunk has started
        elif line.startswith("Reply") and start: 
            # Add the current chunk to the list of chunks
            chunks.append(chunk)
            # Start a new empty chunk
            chunk = []
            start = False

        # If a chunk has started, add the line to the current chunk
        elif start:
            chunk.append(line.strip())


dic = {} # an empty dictionary to store the comments of each user
users_with_multiple_posts = set() # a set to store users who posted multiple comments
users = set() # a set to store all users who posted comments

for chunk in chunks:

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

print(list(users))
print(list(users_with_multiple_posts))

mentions = [] # an empty list to store users who mentioned "cough", "cold", or "fever"

for user, comments in dic.items():
    for comment in comments:
        # If the comment mentions the words "cough", "cold", or "fever", add the user and all their comments to the list of mentions
        if "cough" in comment or "cold" in comment or 'fever' in comment:
            mentions.append(user)
            break   

print(mentions)