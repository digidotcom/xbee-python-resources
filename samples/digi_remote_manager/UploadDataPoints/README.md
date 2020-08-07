Upload Data Points Sample Application
=====================================

This sample Python application shows how to upload data to Digi Remote Manager.

The example reads the internal temperature value from the Digi device and
uploads it to Digi Remote Manager through data streams every 10 seconds.

Requirements
------------
To run this example you will need:

* A Digi Cellular router or XBee gateway device.
* A Digi Remote Manager account with your Digi device added to it.
  Go to https://myaccount.digi.com/ to create it if you do not have one.

Setup
-----
1. Make sure that the Digi Device is connected to Internet and it is registered
   in your Digi Remote Manager account.

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Upload Data Points** application in the Digi device. The
   application starts uploading data to Digi Remote Manager, you will notice it
   because the application prints the following line every time a Data Point is
   uploaded:
   
       - Uploading data '46.938' to stream 'deviceTemperature'

2. In your Digi Remote Manager account, go to **Data Services > Data Streams**
   and verify that there is a data stream called:
   
       00000000-00000000-XXXXXXXX-XXXXXXXX/deviceTemperature
   
   where:
   
   - `00000000-00000000-XXXXXXXX-XXXXXXXX` is the device ID of your Cellular
     Router or  XBee Gateway device.

3. Select the data stream and verify the values are being updated periodically
   both in the table and the graph.

Supported platforms
-------------------
* 6300-CX
* 6310-DX
* 6330-MX
* 6350-SR
* EX12
* EX15
* TX54
* TX64
* IX10
* IX14
* IX15
* IX20

License
-------
Copyright (c) 2020, Digi International, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
