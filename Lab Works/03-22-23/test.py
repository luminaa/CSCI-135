import collections

# extract chunks from a file
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
                if line.strip() == "Comment deleted by user" or line.strip() == 'Comment removed by moderator':
                    chunk = []
                    start = False
                    continue
                chunk.append(line.strip())

    return chunks


# extract users, comments, and users with multiple posts from chunks
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


# extracts all users and their posts that mentions cough, cold, or fever
def get_mentions_with_cough_cold_fever(dic):
    cough_cold_fever_mentions = []
    cough_mentions = []
    cold_mentions = []
    fever_mentions = []

    for user, comments in dic.items():
        for comment in comments:
            if "cough" in comment and "cold" in comment and "fever" in comment:
                cough_cold_fever_mentions.append([user, comment])
            elif "cough" in comment and "cold" not in comment and "fever" not in comment:
                cough_mentions.append([user, comment])
            elif "cold" in comment and "cough" not in comment and "fever" not in comment:
                cold_mentions.append([user, comment])
            elif "fever" in comment and "cough" not in comment and "cold" not in comment:
                fever_mentions.append([user, comment])

    return cough_cold_fever_mentions, cough_mentions, cold_mentions, fever_mentions


def get_users_with_mentions(dic):
    users_with_mentions = []
    for user, comments in dic.items():
        for comment in comments:
            if "cough" in comment or "cold" in comment or "fever" in comment:
                users_with_mentions.append(user)
    return users_with_mentions


def get_top_ten_users(dic):
    user_counter = collections.Counter(dic)
    sorted_user_counter = sorted(user_counter.items(), key=lambda x:x[1])
    top_ten_users = sorted_user_counter[:10]
    top_ten_users_names = [names[0] for names in top_ten_users]
    return top_ten_users_names


file_path = "daily_discussion_april_12.txt"
chunks = get_chunks_from_file(file_path) # TASK(a)

dic, users, users_with_multiple_posts = get_users_comments_from_chunks(chunks) 

cough_cold_fever_mentions, cough_mentions, cold_mentions, fever_mentions = get_mentions_with_cough_cold_fever(dic) # TASK (b) & TASK (c)

users_with_mentions = get_users_with_mentions(dic) # TASK (d)

top_ten_users = get_top_ten_users(dic) # TASK (e) & TASK (f)

print("TASK (a) Done!")
print(f"TASK (b) Number of posts that mention cough, cold, and fever together: {len(cough_cold_fever_mentions)}")
print(f"TASK (c)(i) Number of posts that mention cough (with no mention of the other symptoms): {len(cough_mentions)}")
print(f"TASK (c)(ii) Number of posts that mention cold (with no mention of the other symptoms): {len(cold_mentions)}")
print(f"TASK (c)(iii) Number of posts that mention fever (with no mention of the other symptoms): {len(fever_mentions)}")
print(f"TASK (d) Number of posts that mention cough, cold, or fever: {len(users_with_mentions)}")
print(f"TASK (e) Done!")
print(f"TASK (f) Names of the top ten users with most number of posts: {top_ten_users}")