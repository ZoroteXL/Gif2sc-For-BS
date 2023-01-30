import cv2
import os
import json
import re
import jt
from PIL import Image


with open('out.json', 'w') as out_file:
  template = open('template.json', 'r')
  out_file.write(template.read())

inputfile = input("File name: ")

vidcap = cv2.VideoCapture(inputfile)
success,image = vidcap.read()

fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(f"FPS: {fps}")

if os.path.isdir("frames\\"):
  if os.listdir("frames\\") != []:
    for f in os.listdir("frames\\"):
      os.remove(os.path.join("frames\\", f))
else:
  os.mkdir("frames\\")

lst = []
for f in os.listdir("frames\\"):
  lst.append("frames\\"+ f)

jt.video_to_frames(inputfile)
jt.image_compose()
def num_sort(test_string):
  return list(map(int, re.findall(r'\d+', test_string)))[0]
lst.sort(key=num_sort)

im = Image.open('out_tex.png')
width, height = im.size

files_number = len(os.listdir("frames\\"))

def write_json(new_data,arrayf,filename='out.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)

def write_json0(new_data,arrayf,arrayg,arrayb,filename='out.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf][arrayg][arrayb].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)

def write_json3(arrayf,filename='out.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    if arrayf == "width":
      file_data["textures"][0][arrayf] = width
    else:
      file_data["textures"][0][arrayf] = height
    file.seek(0)
    json.dump(file_data,file,indent=4)

def write_json1(new_data,arrayf,arrayg,arrayb,arrayc,filename='out.json'):
  with open(filename,'r+') as file:
    file_data = json.load(file)
    file_data[arrayf][arrayg][arrayb][arrayc].append(new_data)
    file.seek(0)
    json.dump(file_data,file,indent=4)

bitmaps= {"id":0,"bitmaps":[{"textureIndex":0,"isRectangle":False,"points":[{"twip":[0,-1024],"uv":[1,1]},{"twip":[1024,-1024],"uv":[1,1]},{"twip":[1024,1],"uv":[1,1]},{"twip":[0,1],"uv":[1,1]}]}]}
bindId = {"bindId":0,"blend":0,"name":None}
movieClip = {"id":1000,"frameRate":60,"binds":[],"data":{"frames":[],"grids":[],"values":[]},"names":["GIF2SC"]}
transforms = {"name":None,"transforms":[{"bindIndex":0}]}
id1005 = {"id":1005,"frameRate":25,"binds":[{"bindId":1003,"blend":0,"name":"txt"}],"data":{"frames":[{"name":None,"transforms":[{"bindIndex":0}]}],"grids":[],"values":[]}}
id1001 = {"id":1001,"frameRate":60,"binds":[{"bindId":1000,"blend":0,"name":None},{"bindId":1005,"blend":0,"name":None}],"data":{"frames":[{"name":None,"transforms":[{"bindIndex":0,"matrix":[[0.2529296875,0,-130],[0,0.099609375,51]]},{"bindIndex":1,"matrix":[[0.2998046875,0,-130],[0,0.2998046875,-30]]}]}],"grids":[],"values":[]},"names":["GIF2SC"]}
movieClip["frameRate"] = fps
write_json(movieClip, "movieClips")
write_json(id1005, "movieClips")
write_json(id1001, "movieClips")

write_json3("width")
write_json3("height")
tiles_count_w = width / 536
tiles_count_h = height / 536
all_width = 0
all_height = 0
huy_tadzhika = 0
for i in range(0, files_number):
  transforms["transforms"][0]["bindIndex"] = i
  bindId['bindId'] = i
  movieClip["binds"] = bindId
  write_json0(movieClip["binds"],"movieClips",0,"binds")
  write_json1(transforms,"movieClips",0,"data","frames")
  if huy_tadzhika == 15:
    huy_tadzhika = 0
    all_height += 536
  bitmaps = {"id": i,"bitmaps": [{"textureIndex": 0,"isRectangle": False,
                                  "points": [{"twip": [0.0,-1024.0],"uv": [536 * huy_tadzhika,all_height]},{"twip": [1024.0,-1024.0],"uv": [536 + 536*huy_tadzhika,all_height]},
                                             {"twip": [1024.0,1.0],"uv": [536 + 536*huy_tadzhika,all_height + 536]},{"twip": [0.0,1.0],"uv": [536*huy_tadzhika,all_height + 536]}]}]}
  write_json(bitmaps,"shapes")
  huy_tadzhika += 1

