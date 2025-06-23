from tabulate import tabulate

class Membership:
  def __init__ (self):
      self.database = [{'membership': 'Platinum', 'Discount': '15%' , 'Another Benefit' : 'Gold, Liburan, Cashback'}, 
        {'membership': 'Gold', 'Discount': '10%' , 'Another Benefit' : 'Silver, Voucer Gojek'},
        {'membership': 'Silver', 'Discount': '8%' , 'Another Benefit' : 'Voucer Makan'}]

      self.membership_req = [{'Membership': 'Platinum', 'Monthly Expense': 8, 'Monthly Income': 15}, 
                              {'Membership': 'Gold', 'Monthly Expense': 6,'Monthly Income': 10}, 
                              {'Membership': 'Silver', 'Monthly Expense': 5, 'Monthly Income': 7}] 

  def show_benefit(self):
      print (tabulate(self.database,headers='keys'))

  def show_requirements(self):
      print (tabulate(self.membership_req,headers='keys', tablefmt='grid'))

  def predict_membership(self, user_expense:int, user_income:int):
      #r_value_plat = ((user_expense-self.membership_req[0]['Monthly Expense'])**2 + (user_income-self.membership_req[0]['Monthly Income'])**2)**(1/2)
      #r_value_gold = ((user_expense-self.membership_req[1]['Monthly Expense'])**2 + (user_income-self.membership_req[1]['Monthly Income'])**2)**(1/2)
      #r_value_silver = ((user_expense-self.membership_req[2]['Monthly Expense'])**2 + (user_income-self.membership_req[2]['Monthly Income'])**2)**(1/2)

      jarak = []
      for item in self.membership_req: #untuk setiap dictionary di member_req
        r_value = ((user_expense- item ['Monthly Expense'])**2 + (user_income- item ['Monthly Income'])**2)**(1/2)
        jarak.append(r_value)
      angka_terdekat = min(jarak) #harus d luar for. biar programnya jalan 1x AJA, tidak 3x

      indeks_angka_terdekat = jarak.index(angka_terdekat) #kita nyari INDEKS untuk melacak nilai angka terkecil di list jarak
      tier_user = self.membership_req[indeks_angka_terdekat]['Membership'] #manggil golongan membership
      print(f'Berdasarkan penghasilan dan pengeluaran, kamu layak jadi member {tier_user}')

  def calculate_price(self, membership, list_harga_barang):
    total_harga = sum(list_harga_barang)

    if membership == 'Platinum':
      diskon = 0.15
    elif membership == 'Gold':
      diskon = 0.10
    elif membership == 'Silver':
      diskon = 0.08

    final_price = total_harga*(1-diskon)
    print(f'Total harga setelah diskon adalah {final_price}')

        

user1= Membership()
user1.show_benefit()
user1.show_requirements()
user1.predict_membership(7,15) 
list_belanja = [10000, 20000, 700000]
user1.calculate_price('Platinum', list_belanja)

#gimana caranya manggil (list, dict in list,)