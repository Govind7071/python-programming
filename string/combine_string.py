#combine  two individual strings
name="govind"
course="\tfrom B.tech"
bio="bio=bio is not for engineering students\n"
combine=(f"hello everyone,{name}{course}\n{bio}")
print(combine)
print(combine.title())