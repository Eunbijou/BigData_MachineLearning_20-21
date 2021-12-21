a = "Life is too short, you need python"

if "wife" in a:
    print("wife") #x
elif "python" in a and "you" not in a:
    print("python") #x
elif "shirt" not in a:
    print("shirt") #o
elif "need" in a:
    print("need")
else:
    print("none")

#결과 값? shirt
