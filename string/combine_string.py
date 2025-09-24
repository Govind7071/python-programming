#combine  two individual strings
name="govind"
course="\tfrom B.tech"
bio="bio=bio is not for engineering students\n"
combine=(f"hello everyone,{name}{course}\n{bio}")
print(combine)
print(combine.title())
print(len(bio))
print(bio[1])
print(name[-1])
print("is" in bio)
print("govind" in bio)
print("govind" not in bio)
print(bio[1:6])
print(bio[-5:])
print(bio[-5:-1])
print(name.replace("o","v"))
print(course.split(" "))
#stripping white space
lang='python1  '
print(len(lang))
lang=lang.rstrip()# for whitespace in right side
print(len(lang))
info='  favourite'
print(len(info))
info=info.lstrip()# for whitespace in left side
print(len(info))
idea='  no idea  '
print(len(idea))# for whitespace in right and left both
idea=idea.strip()
print(len(idea))