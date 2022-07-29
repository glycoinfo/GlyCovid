from glob import glob

def count_dataset():
    db_dir_list = glob("data/*", recursive=True)
    db_list = [ db_dir.split("/")[1] for db_dir in db_dir_list ]

    count_dataset = {}
    for db in db_list:
        count_dataset[db] = 0
        file_path_list = glob("data/"+db+"/*.tsv")
        for file_path in file_path_list:
            with open(file_path) as f:
                data_tsv = f.read().split("\n")
                count_dataset[db] += len(data_tsv)
    print(count_dataset)


if __name__ == "__main__":
    count_dataset()
