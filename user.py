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

    def check_user_plan(self):
        if(self.current_plan):
            print(f"{self.username} Berlangganan {self.current_plan}")
            print("Benefit")

            idx_current_plan = self.list_plan.index(self.current_plan)
            headers_user = [self.headers[idx_current_plan],self.headers[-1]]
            benefit_user = [[row[idx_current_plan], row[-1]] for row in self.list_benefit]
            print(tabulate(benefit_user, headers_user))
        else:
            print("Belum Berlangganan")


    def upgrade_plan(self, new_plan):
        if(self.current_plan is not None and new_plan in self.list_plan):
            idx_cureent_plan = self.list_plan.index(self.current_plan)
            idx_new_plan = self.list_plan.index(new_plan)

            if(idx_new_plan > idx_cureent_plan):
                if(self.duration_plan > 12):
                    total = self.list_benefit[-1][idx_new_plan] - (self.list_benefit[-1][idx_new_plan]*0.05)
                else:
                    total = self.list_benefit[-1][idx_new_plan]
                print(f"Harga Upgrade ke {new_plan} adalah Rp. {total}")

                self.current_plan = new_plan
                for key, value in self.data_user.items():
                    if(self.username == value[0]):
                         self.data_user[key][1] = new_plan
                         break
                    

            elif(idx_cureent_plan == idx_new_plan):
                print(f"Anda sedang berlangganan {new_plan}")
            else:
                print(f"Anda tidak bisa downgrade kw {new_plan}")

        elif(new_plan not in self.list_plan):
            print("New Plan tidak tersedia")
        elif(self.current_plan is None):
            print("Silahkan berlangganan terlebih dahulu")

    def subs_plan(self, new_plan, code_referral):
        list_code = [row[-1] for row in self.data_user.values()]

        if(self.current_plan is None):

            if(new_plan in self.list_plan):
                self.current_plan = new_plan
                self.duration_plan = 1
                self.code_referral = f"{self.username}-123"

                idx_new_plan = self.list_plan.index(new_plan)

                if(code_referral in list_code):
                    total = total = self.list_benefit[-1][idx_new_plan] - (self.list_benefit[-1][idx_new_plan]*0.04)
                else:
                    total = self.list_benefit[-1][idx_new_plan]
                print(f"Harga yang dibayarkan untuk subs {new_plan} adalah Rp. {total} ")

                last_key = max(self.data_user.keys())
                self.data_user[last_key+1] = [self.username, self.current_plan, self.duration_plan, self.code_referral]

            else:
                print("Plan tidak ada")

        else:
            print("Anda sudah ada akun")


