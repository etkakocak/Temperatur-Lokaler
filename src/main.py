import network
import socket
from time import sleep
from machine import Pin
import dht
from felsokning import err, ltem, hhum

ssid = 'SSID HERE' 
password = 'PASSWORD HERE' 

sensor = dht.DHT11(Pin(0))

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(o1, o2):
    with open("style.css", "r") as c:
        stylecss = c.read()
    with open("script.js", "r") as j:
        scriptjs = j.read()
    html = f""" <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>Lokal 1</title>
            <style>
            {stylecss}
            </style>
            </head>
            <body>
            <h1>Temperatur Lokal 1</h1>
            <p id="date"></p>
            <table>
            <tr>
            <th>Klockan</th>
            <th>Temperatur (°C)</th>
            <th>Fuktighet (% RH)</th>
            </tr>
            <tr>
            <td id="time"></td>
            <td>{o1}</td>
            <td>{o2}</td>
            </tr>
            </table>
            <script>
            {scriptjs}
            </script>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    while True:
        try:
            sensor.measure()
        except:
            err()
        try:
            client = connection.accept()[0]
            temp = sensor.temperature()
            hum = sensor.humidity()
            o1 = ('%3.1f' %temp)
            if temp < 20:
                ltem()
            o2 = ('%3.1f' %hum)
            if hum < 30 or hum > 50:
                hhum()
        except IndexError:
            pass      
        html = webpage(o1, o2)
        client.send(html)
        client.close()
        sleep(3600)

try:
    ip = connect()
    print("1- Sucess")
    connection = open_socket(ip)
    print("2- Sucess")
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
