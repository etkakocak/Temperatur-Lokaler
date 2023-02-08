# Test
## main.py
The program ``main.py`` can be tested by connecting the device to a computer and opening the program files through the Thonny IDE. When you write the SSID and password for Wi-Fi, you can run the program for testing.  
``Expected output:``  
```
Waiting for connection...  
Waiting for connection...
Connected on {IP-adress}
1- Sucess
2- Sucess
```
## Device
The device itself can be tested by connecting to an outlet and opening the website to be able to see the results of temperature and humidity measurement. In a room at body temperature it should give a normal result such as 22.3° C and 41.5%. If you plug it into an outlet or power bank out there, the blue light should flash to say it's below body temperature and the temperature measurement result should be much less than 20°C if it's cold outside.  
The temperature and humidity data is updated every hour, so you can test in a room, measure the temperature and then open a window and let the room be cold and see the result updated in 1 hour and it is much less than previous results.  