names = ["Bam", "Jam", "Pam"]
length = len(names)
if length == 3:
    answer = ", ".join(names[:2]), "and", "".join(names[2]), "like this"
    print(" ".join(answer))
elif length == 2:
    print(", ".join(names[:1]), "and", "".join(names[1]), "like this")
elif length == 1:
    print("".join(names[:]), "likes this")
elif length == 0:
    print("no one likes this")
else:
    print(", ".join(names[:2]), "and", str(length - 2), "others like this")

answer = ", ".join(names[:1]), "and ".join(names[1]), "like this"
answer_2 = "".join(answer)
print(type(answer_2))





