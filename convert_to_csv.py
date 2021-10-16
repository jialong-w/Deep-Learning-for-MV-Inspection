# Author: Jialong Weng
# Convert annotations.json into csv for data processing for yolo

import os
import ast
import csv
import json

DATA_PATH = "dataset/"

if __name__ == "__main__":
    header = ['file_name', 'height', 'width', 'categories', 'bbox']
    with open(os.path.join(DATA_PATH, "annotations.csv"), 'w', encoding='UTF8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # write the header
        writer.writerow(header)

        # read json file
        with open(os.path.join(DATA_PATH, "annotations.json"), 'r') as json_file:
            # parse file
            obj = json.loads(json_file.read())
            images = obj["images"]
            annotations = obj["annotations"]
            image_id = int(annotations[0]["image_id"])
            bbox = []
            categories = []
            for i in range(len(annotations)):
                prev_image_id = image_id
                image_id = int(annotations[i]["image_id"])
                if image_id == prev_image_id:
                    bbox.append(annotations[i]["bbox"])
                    categories.append(annotations[i]["category_id"])
                else:
                    # write data to csv
                    id = prev_image_id - 1
                    file_name = images[id]["file_name"]
                    height = images[id]["height"]
                    width = images[id]["width"]
                    data = [file_name, height, width, categories, bbox]
                    writer.writerow(data)
                    # update bbox and categories
                    bbox = [annotations[i]["bbox"]]
                    categories = [annotations[i]["category_id"]]

            # write last data to csv
            id = prev_image_id - 1
            file_name = images[id]["file_name"]
            height = images[id]["height"]
            width = images[id]["width"]
            data = [file_name, height, width, categories, bbox]
            writer.writerow(data)
