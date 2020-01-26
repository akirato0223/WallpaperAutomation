
import requests
import wget
import subprocess
import time


def get_wallpaper():
    url = 'https://api.unsplash.com/photos/random/?client_id=4180d9ba77746652d711753e7d1dc86431d876a0933af0600d6e61f02dcadddd'
    params = {
        "query": "HD Wallpapers",
        "orientation": "landscape"
    }
    res = requests.get(url).json()
    image_url = res['urls']['full']
    # download the wallpaper
    image = wget.download(image_url, '/tmp/wallpaper.jpg')
    return image

def change_wallpaper():
    	wallpaper = get_wallpaper()
	cmd = """/usr/bin/osascript<<END
	tell application "Finder"
	set desktop picture to POSIX file "%s"
	end tell
	END"""

	subprocess.Popen(cmd%wallpaper, shell=True)
	subprocess.call(["killall Dock"], shell=True)

def main():
	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nHope you like this one! Quitting.")
	except Exception as e:
		pass
	
if __name__ == "__main__":
    	main()
