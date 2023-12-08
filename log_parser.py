import re

pattern = re.compile('^.*(WARNING).*$', re.MULTILINE)

with open('data/rsvp_agent_log.dat', mode="r") as f:
    # file = f.read()
    # results = re.findall(pattern, file)
    lines = f.readlines()
    for line in lines:
        if re.match(pattern, line):
            print(line)



