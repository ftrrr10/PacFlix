from tabulate import tabulate


class User:
    data_user = {
        1: ["Rosy", "Basic Plan", 12, "rosy-123"],
        2: ["sun", "Standard Plan", 8, "sun-123"],
        3: ["Ciwil", "Premium Plan", 13, "ciwil-123"],
        4: ["Oppa", "Basic Plan", 2, "oppa-123"],
        5: ["Yunbin", "Standard Plan", 22, "yunbin-123"],
        6: ["Daebak", "Basic Plan", 14, "daebak-123"]
    }

    list_plan = ["Basic Plan", "Standard Plan", "Premium Plan"]
    list_benefit = [
        [True, True, True, "Bisa Stream"],
        [True, True, True, "Bisa Download"],
        [True, True, True, "Kualitas SD"],
        [False, True, True, "Kualitas HD"],
        [False, False, True, "Kualitas UHD"],
        [1, 2, 4, "Number of Devices"],
        ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
        [120_000, 160_000, 200_000, "Harga"]
    ]

    headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

    def __init__(self, username):
        self.username = username
        self.current_plan = None
        self.duration_plan = None
        self.code_referral = None

        # Cari data user berdasarkan username
        for key, value in User.data_user.items():  # Gunakan User.data_user
            if value[0] == self.username:
                self.current_plan = value[1]
                self.duration_plan = value[2]
                self.code_referral = value[3]
                break

        # Jika user tidak ditemukan
        if self.current_plan is None:
            print(f"User '{self.username}' tidak ditemukan di data_user.")
    
    def check_all_plan(self):
        
        print("List Benefit dan Plan PacFlix")
        print(tabulate(self.list_benefit, self.headers))
