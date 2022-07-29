def get_id_set(row):
    id_set = [ column.split(":")[0] for column in row ]
    id_set[2] = "-2"
    id_set[3] = "-3"
    id_set[4] = "-4"
    id_set[5] = "-5"
    id_set[6] = "-6"
    id_set[7] = "-7"
    return id_set


class PQdataList:
    def __init__(self):
        self.data = []

    def add(self, row):
        assert(type(row) == list)

        row_data = []
        id_set = get_id_set(row)
        if self.has_same_id_set(row):
            self.get_same_id_pqdata(row).add(row)
        else:
            self.data.append(
                    PQdata(id_set, row)
                )

    def has_same_id_set(self, row):
        for pqdata in self.data:
            if pqdata.is_same_id_set(row):
                return True
        return False

    def get_same_id_pqdata(self, row):
        for pqdata in self.data:
            if pqdata.is_same_id_set(row):
                return pqdata



class PQdata:
    def __init__(self, id_set:list, row):
        self.id_set = id_set
        self.row_list = [row]

    def is_same_id_set(self, row):
        id_set = get_id_set(row)
        if self.id_set == id_set:
            return True
        return False

    def add(self, row):
        self.row_list.append(row)

