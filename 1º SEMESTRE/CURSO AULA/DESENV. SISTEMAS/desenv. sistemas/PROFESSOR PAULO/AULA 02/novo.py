
def inverter(l = ""):
    if len(l.len) > 0:
        print(l[-1])
        inverter(l[:-1])

inverter("python")