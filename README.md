# KVIHACKER
Hacking CLI app with free Midjourney, fake person data generator, fake fingerprints generator, DDos attacks etc.

## Options
Usage: main.py [-h] [-imagine IMAGINE] [-name NAME] [-ip IP] [-fake FAKE] -m M [-t TARGET] [-p PORT] [-np NUM_PACKETS]
               [-ps PACKET_SIZE] [-url URL]

Options:
  -h, --help            show this help message and exit
  -imagine IMAGINE      Text to imagine in the image
  -name NAME            Generate fingerprints based on text input
  -ip IP                Get full IP info
  -fake FAKE            Generate fake data
                        (name/lastname/adress/text/email/phone/date/creditCard/job/domain/paragraph)
  -m M                  Model name to use (can be: mj, finger, ip, fake, ddos, gethtml, getcss)
  -t TARGET, --target TARGET
                        Target IP address
  -p PORT, --port PORT  Target port number
  -np NUM_PACKETS, --num_packets NUM_PACKETS
                        Number of packets to send (default: 500)
  -ps PACKET_SIZE, --packet_size PACKET_SIZE
                        Packet size in bytes (default: 64)
  -url URL              Get something from this url

## Get started

Install required libraries:
```Bash
pip install argparse halo bs4 faker scapy
```
Clone repository:
```Bash
git clone https://github.com/Vasiliy-katsyka/KVIHACKER
cd KVIHACKER
```
Run code, using instruction that i've described at the top:
```Bash
python3 main.py [-h] [-imagine IMAGINE] [-name NAME] [-ip IP] [-fake FAKE] -m M [-t TARGET] [-p PORT] [-np NUM_PACKETS]
               [-ps PACKET_SIZE] [-url URL]
```

## Help & Contribute
Help & Contribute - kviappsgames@gmail.com
