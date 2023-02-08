# Setup

**The device's setup is not done by the user but by a developer.** When we have received the order, we ask for the premises' Wi-Fi SSID and password to be able to enter it into the device's code. We also create a website for the user to get the device data. Then we send it as ready to use with the link of the website. 

## Setup Guide for developer:

### 1. Wi-Fi
Connect the device to a computer and open the ``Thonny IDE``. Open ``main.py`` enter the SSID and password of the user's Wi-Fi as strings. Don't forget to save the code.

```python
#main.py line 8, 9
ssid = 'SSID HERE' 
password = 'PASSWORD HERE' 
```

### 2. Website
Open ``Repl.it`` which we used to build websites. Create a copy of our website with the user's premises name. E.g.: **Room 1**, **lounge**, **library floor 1**. Enter the ``IP address`` of the Raspberry Pi Pico W device in the code ``index.html``.  
```HTML
<!-- index.html line 16 -->
<a href="IP-adress here">premises name</a>
```

### 3. Send
Send the ready-to-use device to the user and also send the website link as an email to the user.  