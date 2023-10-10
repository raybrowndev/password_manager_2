import datetime

class PasswordManager2():
    def __init__(self):
        self.pw_manager = { "all": []}
        # self.pw_manager = { "all" [{"service": 'gmail', "password": '12ab5!678', "added_on": "22/08"}]}
    def add(self, given_service,given_password):
        if not any(entry["password"] == given_password for entry in self.pw_manager["all"]) and not any(entry["service"] == given_service for entry in self.pw_manager["all"]):
            if (len(given_password) > 7 and any(char in given_password for char in ["!", "@", "$", "%", "&"])):
                    new_entry = {
                        "service": given_service,
                        "password": given_password,
                        "added_on": datetime.datetime.now()
                    }

                    self.pw_manager["all"].append(new_entry)

    def remove(self, given_service):
        self.pw_manager["all"] = [entry for entry in self.pw_manager["all"] if entry["service"] != given_service]
    
    def update(self, given_service, given_password):
        for i in self.pw_manager["all"]:
            if not any(entry["password"] == given_password for entry in self.pw_manager["all"]):
                if (len(given_password) > 7 and any(char in given_password for char in ["!", "@", "$", "%", "&"])):
                    i["password"] = given_password
                    i["service"] = given_service

    def list_services(self):
        all_pw = self.pw_manager["all"]
        service_list = [item["service"] for item in all_pw]
        return service_list

    def sort_services_by(self,type, reverse=False):
        if type == "service":
            sorted_list = sorted(self.pw_manager["all"], key=lambda x: x["service"])
        elif type == "added_on":
            sorted_list = sorted(self.pw_manager["all"], key=lambda x: x["added_on"])
        elif type == "service" and reverse == "reverse":
            sorted_list = sorted(self.pw_manager["all"], key=lambda x: x["service"])
        else:
            return self.pw_manager

        if reverse:
            sorted_list.reverse()

        all_pw = sorted_list
        service_list = [item["service"] for item in all_pw]
        return service_list


    def get_for_service(self,given_service):
        for item in self.pw_manager["all"]:
            if item["service"] == given_service:
                return item["password"]
