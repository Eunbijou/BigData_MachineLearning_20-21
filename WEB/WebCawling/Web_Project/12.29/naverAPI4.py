json = {'name' : 'Kyeongrok',
        'age' : '32',
        'where' : '역삼동',
        'phone_number' : '010-1234-5678',
        'friends' : [{"name" : "sian", "age" : "32"},
                     {"name" : "kyuri", "age" : "32"}]}

# print(json.keys())

# print(json['name'])
# print(json['phone_number'])

friends = json['friends']
for friend in friends:
    print(friend["name"])
    print(friend["age"])