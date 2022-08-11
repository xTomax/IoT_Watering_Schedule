def web_page(relays, relays_names):
    # Set relay_state variable based on state returned from output pins
    relays_html = list()
    for relay in relays:
        if relay.value() == 1:
            relays_html.append("ON")
        else:
            relays_html.append("OFF")

    # Create a variable containing the HTML to be sent
    # The state of the relays are contained in the variables we have just set
    html_head = """<html>
      <head> 
        <title>IoT Watering System</title> 
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;} h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #006400; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}.button2{background-color: #dc143c;}</style>
      </head>
      <body> 
        <h1>IoT Watering System</h1>"""
    html_body_relay = ""
    i = 0
    for relays_name in relays_names:
        i = i+1
        html_body_relay = html_body_relay + """<p>Estado {0}: <strong>{1}</strong></p>
        <p>
          <a href="/?relay{2}=on"><button class="button">ON</button></a>
          <a href="/?relay{2}=off"><button class="button button2">OFF</button></a>
        </p>
        <label for="monday">Mon:</label>
        <input type="checkbox" id="monday" name="monday" value="true">
        <label for="tuesday">Tue:</label>
        <input type="checkbox" id="tuesday" name="tuesday" value="true">
        <label for="wednesday">Wed:</label>
        <input type="checkbox" id="wednesday" name="wednesday" value="true">
        <label for="thursday">Thu:</label>
        <input type="checkbox" id="thursday" name="thursday" value="true">
        <label for="friday">Fri:</label>
        <input type="checkbox" id="friday" name="friday" value="true">
        <label for="saturday">Sat:</label>
        <input type="checkbox" id="saturday" name="saturday" value="true">
        <label for="sunday">Sun:</label>
        <input type="checkbox" id="sunday" name="sunday" value="true">
        """.format(relays_name, relays[i-1], i)
    html_body_relay = html_body_relay + """</body>
    </html>"""
    # Return the HTML
    return html_head + html_body_relay

