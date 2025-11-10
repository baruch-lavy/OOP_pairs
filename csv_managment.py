from library import Library
import csv
class FileManegment:
    def csv_write(path,data_to_write):
        field_names = data_to_write.keys()
        data = data_to_write
        with open(path,'a',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            if Library.is_new_book:
                writer.writeheader()
                Library.is_new_book = False
            writer.writerow(data)