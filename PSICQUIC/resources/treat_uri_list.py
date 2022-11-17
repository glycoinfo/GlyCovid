import csv

def csv_to_dict():
    # 両末端のスペースを取る？
    csv_dict = dict()
    with open("uri_list/object_uri_list.csv") as f1:
        reader = csv.reader(f1, delimiter=",")
        next(reader)
        for row in reader:
            csv_dict[row[0]] = dict()
            csv_dict[row[0]]['uri'] = row[1]
            try:
                csv_dict[row[0]]['uri_example'] = row[2]
            except:
                pass
            try:
                csv_dict[row[0]]['psiquic_class'] = row[3]
            except:
                pass
    return csv_dict

def add_data_in_dict(object_uri_list):
    with open("uri_list/out.csv") as f1:
        reader = csv.reader(f1, delimiter=",")
        for row in reader:
            try:
                object_uri_list[row[0]]["psiquic_data"] = row[1]
            except:
                object_uri_list[row[0]] = dict()
                object_uri_list[row[0]]["psiquic_data"] = row[1]
    return object_uri_list

def dict_to_csv(object_uri_list: dict):
    file_text = "database, uri, uri_example, psiquic_data\n"
    print(object_uri_list)
    for key in object_uri_list:
        file_text += key
        try:
            file_text += "," + object_uri_list[key]["uri"]
        except:
            file_text += ","
        try:
            file_text += "," + object_uri_list[key]["uri_example"]
        except:
            file_text += ","
        try:
            file_text += "," + object_uri_list[key]["psiquic_data"]
        except:
            file_text += ","
        file_text += "\n"

    return file_text


def main():
    object_uri_list = csv_to_dict()

    object_uri_list = add_data_in_dict(object_uri_list)

    object_uri_text = dict_to_csv(object_uri_list)
    f = open("uri_list/object_uri_list2.csv", "w")
    f.write(object_uri_text)
    f.close()



if __name__ == "__main__":
    main()
