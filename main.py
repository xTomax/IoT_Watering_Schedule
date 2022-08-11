# GPIO ARRAY List
# relayArray = [16, 14, 12, 13, 15, 0, 4, 5]
import html_data
import Utils
import machine

try:
    import usocket as socket
except:
    import socket
# GPIO ARRAY List
relayArray = [16, 14, 12, 13, 15, 0, 4, 5]
RELAYS = [machine.Pin(i, machine.Pin.OUT) for i in relayArray]
relays_names = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
#default_relay_names = ['relay1', 'relay2', 'relay3', 'relay4', 'relay5', 'relay6', 'relay7', 'relay8']
# Create a socket we will use for webserver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind this socket to port 80
s.bind(('', 80))
# Listen on the socket
s.listen(5)
read = Utils.read_relaynames()
if read:
    relays_names = read.strip()

while True:
    # Accept a connection on port 80
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    # Recieve a request from the client
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    for relay in RELAYS:
    relay1_on = request.find('/?relay1=on')
    relay1_off = request.find('/?relay1=off')
    if relay1_on == 6:
        print('Relay 1 ON')
        relay1.value(1)
    if relay1_off == 6:
        print('Relay 1 OFF')
        relay1.value(0)
    relay2_on = request.find('/?relay2=on')
    relay2_off = request.find('/?relay2=off')
    if relay2_on == 6:
        print('Relay 2 ON')
        relay2.value(1)
    if relay2_off == 6:
        print('Relay 2 OFF')
        relay2.value(0)
    response = html_data.web_page(RELAYS, relays_names)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
