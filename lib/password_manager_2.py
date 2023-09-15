# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

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
                        "password" : given_password,
                        "added_on" : datetime.datetime.now()
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