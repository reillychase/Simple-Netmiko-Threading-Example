# Simple Netmiko Threading Example

## Background story
I recently wrote a Python/Netmiko script to download a new IOS image onto 70 Cisco switches over FTP. My original script was handling the task sequentially, and with each image taking about 30 minutes to download, it would've taken about 18 hours to complete. So I looked into threading it. Being able to run all the downloads at the same time reduced the completeion time by 17 hours or so.

I foud this script which was a big help https://gist.github.com/ktbyers/8005564c5d3711a0e5476dbfd18d8acf and I have modified it to add some comments and make it even simpler to understand

I also made a short YouTube video to explain it https://www.youtube.com/watch?v=SnpTBHAX0Mo

## How to Thread your Netmiko script
main.py is a simple example of threading Netmiko with comments on where to place your code
