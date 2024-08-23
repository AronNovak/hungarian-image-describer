import cv2
import argparse
import base64
import requests
import sys
import json
import os

os.environ['QT_QPA_PLATFORM'] = 'xcb'

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

def encode_image(image):
    _, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')

def describe_image(api_key, image):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }

    payload = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Meséld el magyarul, hogy mit látsz a képen 5 mondatban"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": encode_image(image)
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")
        return None

    try:
        return response.json()['content'][0]['text']
    except (KeyError, IndexError) as e:
        print(f"Error: Unexpected response format. Error: {e}")
        print(f"Full response: {json.dumps(response.json(), indent=2)}")
        return None

def speak_text(text):
    os.system(f'espeak-ng -v hu -p 50 -s 130 "{text}"')

def main():
    parser = argparse.ArgumentParser(description="Capture and describe images using Anthropic API")
    parser.add_argument("api_key", help="Anthropic API Key")
    args = parser.parse_args()

    while True:
        input("Press Enter to capture an image...")
        image = capture_image()
        cv2.imshow("Captured Image", image)
        cv2.waitKey(1)
        description = describe_image(args.api_key, image)
        if description:
            print(description)
            speak_text(description)
        else:
            print("Failed to get description.")
        print("\n" + "-"*50 + "\n")
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
