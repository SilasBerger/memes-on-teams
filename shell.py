import requests
import os


API_BASE_URL = "http://localhost:58179/api/template"
TEMPLATE_NAME="memes-on-teams"


def run_animation(animation_name):
  requests.post('%s/%s/data/animation/%s' % (API_BASE_URL, TEMPLATE_NAME, animation_name))

def image_in():
  run_animation("ImageIn")


def image_out():
  run_animation("ImageOut")


def get_image_filenames():
  return [filename for filename in os.listdir("./template/assets/memes") if not filename.startswith(".")]


def list_images():
  image_names = [remove_extension(file_name) for file_name in get_image_filenames()]
  print(image_names)


def remove_extension(file_name):
  return ".".join(file_name.split(".")[:-1])


def send_set_image_request(image_filename):
  url = '%s/%s/data/image' % (API_BASE_URL, TEMPLATE_NAME)
  headers = {
    "Content-Type": "application/json"
  }
  req_body = {
    "id": "image-container",
    "asset": 'memes/%s' % image_filename
  }
  requests.post(url, headers=headers, json=req_body)


def set_image(image_name):
  file_names = [file_name for file_name in get_image_filenames() if remove_extension(file_name) == image_name]
  if len(file_names) > 1:
    print('ERROR: Arbitrary file resolution for image name %s' % image_name)
    return
  if len(file_names) < 1:
    print('ERROR: Unknown image "%s"' % image_name)
    return
  send_set_image_request(file_names[0])
  

def main():
  while True:
    command = input('[show <image_name> | hide | list]: ') 
    if command.startswith("show"):
      image_name = " ".join(command.split(" ")[1:]).replace("\"", "")
      set_image(image_name)
      image_in()
    elif command == "hide":
      image_out()
    elif command == "list":
      list_images()
    else:
      print('ERROR: Unrecognized command: "%s"' % command)


if __name__ == "__main__":
  main()