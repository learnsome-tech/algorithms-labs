def find_user(user_id, users):
    for u in users:
        if u == user_id:
            return True
    return False

users = ['alice', 'bob', 'carol', 'dave', 'eve']
print(find_user('carol', users))
print(find_user('zara', users))
