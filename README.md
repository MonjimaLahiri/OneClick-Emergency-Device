# OneClick-Emergency-Device
Bluetooth Emergency Device | Computer Networks Project 

## Purpose & Methodology
Our project aims to develop a discreet, cost-effective, and compact personal safety device. To ensure reliable and efficient operation, we planned to utilize webhooks and scripting to automate the process.

By integrating a Flic 2 button with a Raspberry Pi, we aim to create a system that sends SMS alerts with GPS location when activated. The Flic 2 button, acting as a discreet emergency trigger, will transmit a signal to the Raspberry Pi. The Raspberry Pi is the signal receiving server. We install the Flic SDK onto the server to detect the button signals. In the meanwhile, we developed a python program to interact with Flic SDK. The program is also able to receive the GPS locations provided by Google API. After the signal detection and GPS information gathering, the Raspberry Pi will send the SMS via Twilio.

Current challenges include reliance on third-party services like Flic Hub and IFTTT, as well as the absence of visual confirmation for alerts.

Our future improvements may include developing a dedicated mobile app for remote control and monitoring, integrating additional sensors for advanced features, and implementing visual and auditory alerts on the device itself.

---

## Data/Result Analysis
- **Flic 2 Connectivity Range:** Up to 50 meters (Utilizing Official Flic SDK)  
  - *Purpose:* Effectiveness of connectivity
- **Twilio Message Capability:** 1 message per second
- **Twilio Business Account:** ($15 credit, $0.0079 per SMS text)  
  - *Purpose:* Frequency and volume  
  - So, you can send up to **271 messages for 1 whole week!**
- **Raspberry Pi Zero 2 Power Consumption Rate:** 120mA  
  - *Purpose:* Low power consumption

---

## Accuracy of Google Geolocation API
<p align="left">
  Accuracy of Google Geolocation API:
  <br>
  - **95%** falls within the green circle (10 meters from location)
  <br>
  - **50%** falls within **5 meters** of location
</p>

<p align="right">
  <img src="path/to/image.png" alt="Geolocation Accuracy" width="300">
</p>

*[Watch on Youtube](https://youtu.be/XYfmuQvPTuo)*  
*Contributors: Monjima Lahiri, Nick Stark, Matthew Press, Darren Famisan, Gabriel Jimenez, Yahui Jiang, Ashley Olson*
