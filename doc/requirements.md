# Requirements

* To measure the temperature and humidity every hour.
* Show the result, i.e. the data on the website.
* Able to send data from device to web page with IoT.
* The device must be connected to a power source in a room and does not need a battery change.
* Being able to create a website that receives the data from the device and displays it to the user.
* The project must be completed by the submission deadline.
* Device must be connected to Wi-Fi.
* Human labor must be reduced, the temperature must be controllable via the website and no one has to go and check the device.
* An easy-to-use device is offered to customers.
* The device should be cheap, cheap to produce and cheap with power consumption.

## Agile User Story

As a ``premises manager``, ``I want`` a device that automatically measures the temperature and humidity in the premises, ``so that`` I don't have to check it manually and can access measurement data from a website.  
### Criteria:
* A device that can measure temperature and send the data with IoT.  
* A website that can get this data and show it to the user.  

As a ``developer``, ``I want`` a simple and efficient coding to control the device, ``so that`` I can debug and improve the device easily.
### Criteria:
* A Raspberry Pi Pico W device using a simple IDE called Thonny.  
* The device works with Python which is a simple programming language.  

As an ``owner of the device``, ``I want`` to be able to detect if something goes wrong with the device and be able to send the device for service ``so that`` I can trust the device and be satisfied with the product.
### Criteria:
* The device has a red LED that flashes if an error occurs on the device. On the website there is contact information regarding flashing red led.  
* Device has a warranty of 2 years so that it can be sent for service when something goes wrong.  

### Power consumption:  
The device DHT11 uses 3 volts voltage and 70 mA (0.07 A) current and it is always on, ie 24/7. Therefore, we can use the following formula to be able to calculate the energy consumption:
Watts per day = V * A * t  
Where V is the voltage in volts, A is the current in amperes and t is the time the device is on during a day in hours (h) so t = 24. Which makes watts per day = 5.04 W. We divide it by 1000 to get calculate kWh that device consumes per day, 5.04 / 1000 = 0.00504 kWh. Which makes the device consume 0.00504 * 30 = 0.1512 kWh per month. Right now, electricity prices are around SEK 5 per kWh, which means that this energy consumption of device is 75.6 öre per month and almost 9 SEK per year.  
It must be noted that the amps were measured through a digital voltmeter and the calculation of the amps may be a little less or a little higher than the correct results. Therefore, we can say between SEK 8-10 per year for energy consumption.  