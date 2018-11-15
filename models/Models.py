class Merchant:
    def __init__(self, name, category, geocode):
        self.name = name
        self.category = category
        self.lat = geocode["lat"]
        self.lng = geocode["lng"]


class Preferences:
    def __init__(self,emailOptIn=None,categories=None):
        self.emailOptIn = emailOptIn
        self.categories = categories


class ProspectiveBusiness:
    def __init__(self, name, category, address, note):
        self.name = name
        self.category = category
        self.address = address
        self.note = note


class User:
    prospective_business_list = []
    preferences = Preferences();
    def __init__(self,userId,firstName,lastName,address,email,phone):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email
        self.phone = phone

    def set_email_opt_in(self, emailOptIn):
        self.preferences.emailOptIn = emailOptIn

    def get_email_opt_in(self):
        return self.preferences.emailOptIn

    def get_prospective_business_list(self):
        return self.prospective_business_list

    def update_prospective_business_list(self,prospective_business):
        self.prospective_business_list.append(prospective_business)





