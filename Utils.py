
def save_relaynames(relay_names):
    f = open("relay_names", "w")
    for name in relay_names:
        f.write(name + '\n')
    f.close()


def read_relaynames():
    try:
        f = open("relay_names", "w")
        relayNames = f.readlines()
    except:
        relayNames = None
    f.close()
    return relayNames
