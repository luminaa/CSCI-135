def get_chunks_from_file(file_path):
    chunks = []
    chunk = []
    start = False 

    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("level"):
                if chunk != []:
                    chunks.append(chunk)
                chunk = [line.strip()]
                start = True

            elif start:
                if line.strip() == "Comment deleted by user":
                    chunk = []
                    start = False
                    continue
                chunk.append(line.strip())

    return chunks


def get_users_comments_from_chunks(chunks):
    dic = {} 
    users_with_multiple_posts = set() 
    users = set() 

    for chunk in chunks:

        if not chunk:
            continue

        username = chunk[1]

        if username in dic:
            users_with_multiple_posts.add(username)

        users.add(username)

        i = 5
        text = ""

        while i < len(chunk) and not chunk[i].startswith('Reply'):
            text += chunk[i]
            i += 1

        if username not in dic:
            dic[username] = []
        dic[username].append(text)

    return dic, users, users_with_multiple_posts


def get_mentions_with_cough_cold_fever(dic):
    mentions = []

    for user, comments in dic.items():
        for comment in comments:
            if "cough" in comment or "cold" in comment or 'fever' in comment:
                mentions.append([user, comments])
                break   

    return mentions

file_path = "daily_discussion_april_12.txt"

# get the chunks from the file
chunks = get_chunks_from_file(file_path)

# get the users, comments, and users with multiple posts from the chunks
dic, users, users_with_multiple_posts = get_users_comments_from_chunks(chunks)

# get the users who mentioned "cough", "cold", or "fever"
mentions = get_mentions_with_cough_cold_fever(dic)

print(users)
print(len(users_with_multiple_posts))
print(len(mentions))