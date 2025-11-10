import json
class FileManegment:
    def json_write(path,data_to_write,is_update=False): 
        try:   
            with open(path,'r') as file:
                data = json.load(file)
                
        except (json.JSONDecodeError):
            data = []
            
        if not isinstance(data, list):
            data = [data]
            
        if is_update:
            data = data_to_write
        else:
            data.append(data_to_write)
        
            
        with open(path,'w') as file:
            json.dump(data,file,indent=4)