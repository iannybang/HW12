class Film:
    def __init__(self, title):
        self.title = title
        self.year = 1000
        self.description =  ''
        self.director = ''
        self.cast = ''
        self.running_time = 0.0
        self.country = ''
        self.language = ''
        self.rating = 0.0
        self.budget = 0
        self.box_office = 0
        self.profitable = False
        self.oscar_nominated = False
        self.oscar_win = False
        self.trailer = ''
        self.storage_address = ''
        self.upload_file()

    def upload_file(self):
        import os
        current_path = os.getcwd()
        storage_dir = os.path.join(current_path,'film_player','film_storage')
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        for folder in os.listdir(storage_dir):
            if self.title[0].upper() == folder.upper():
                folder_path = os.path.join (storage_dir, folder)
                file_path = os.path.join(folder_path, f"{self.title}.txt")
                self.storage_address = file_path
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                with open(file_path, 'w') as file:
                    file.write(f"Title: {self.title}\n")
                    file.write(f"Year: {self.year}\n")
                    file.write(f"Description: {self.description}\n")
                    file.write(f"Director: {self.director}\n")
                    file.write(f"Cast: {self.cast}\n")
                    file.write(f"Running time: {self.running_time}\n")
                    file.write(f"Country: {self.country}\n")
                    file.write(f"Language: {self.language}\n")
                    file.write(f"Rating: {self.rating}\n")
                    file.write(f"Budget: {self.budget}\n")
                    file.write(f"Box_office: {self.box_office}\n")
                    file.write(f"Profitable: {self.profitable}\n")
                    file.write(f"Oscar_nominated: {self.oscar_nominated}\n")
                    file.write(f"Oscar_win {self.oscar_win}\n")
                    file.write(f"Trailer: {self.trailer}\n")
                    file.write(f"Storage address: {self.storage_address}")

                        

    def get_film_address(self):
        return self.storage_address



#Create new film in the class
film_instance = Film("Inception")

#Get path to the created file
print(f"Storage Address: {film_instance.get_film_address()}")