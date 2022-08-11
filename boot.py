import machine

ssid_ = "Guest"
pass_ = "2good4you"


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network {}... ".format(ssid_))
        sta_if.active(True)
        # For Static IP, uncomment:
        # sta_if.ifconfig(('192.168.1.50', '255.255.255.0', '192.168.1.254', '1.1.1.1'))
        sta_if.connect(ssid_, pass_)
        while not sta_if.isconnected():
            print(".")
            machine.sleep(100)
    print('network config:', sta_if.ifconfig())


def check_connection():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        do_connect()


do_connect()
