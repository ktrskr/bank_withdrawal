class bank:
    bank_name='PAYTM PAYMENTS BANK'
    branch='Noida'
    ifsc='PYTM0123456'
    roi=0.06
    def __init__(self,name,phno,acno,bal,pin):
        self.name=name
        self.phno=phno
        self.acno=acno
        self.pin=pin
        self.bal=bal

    @staticmethod
    def validate():
        return int(input('enter 4 dig pin:'))
    
    def check_balance(self):
        if self.pin == bank.validate():
            print(f'your current balance is {self.bal}')
        else:
            print('incorrect pin....')

    def deposit(self):
        if self.pin == bank.validate():
            amount=int(input('enter amount for deposit:'))
            self.bal+=amount
            print('deposited sucessfull!!!!')
        else:
            print('incorrect pin...')

    def withdraw(self):
        if self.pin ==bank.validate():
            amount=int(input('enter amount for withdraw:'))
            if self.bal>amount:
                self.bal-=amount
                print('withdrawn sucessfully!!!')
            else:
                print('Insufficient balance...')
        else:
            print('incorrect pin')
            
    def change_pin(self):
        if self.pin ==bank.validate():
            pin1=int(input('enter new pin:'))
            pin2=int(input('enter new pin:'))
            if pin1==pin2:
                self.pin=pin1
                print('pin changed sucessfully')
            else:
                print('pin not matched')
        else:
            print('incorrect pin')
    @classmethod
    def change_roi(cls):
        newroi=float(input('enter new roi:'))
        cls.roi=newroi
        
  
        
ramu=bank('ramu',9874561230,23412334,10000,2580)
ravi=bank('ravi',9653154511,42648271,50000,1111)
anwar=bank('anwar',7894561203,42290372,25000,2222)
adam=bank('adam',8794561330,345678561,100,2233)

while True:
    print('-'*30)
    print('select users : ')
    print('ramu :: ravi :: anwar :: adam')
    ch=input()
    if ch=='ramu':
        print('-'*30)
        print('(1) : Deposit\n(2): Withdraw\n(3):check balance\n(4):change pin')
        option=int(input('enter an option:'))
        if option == 1:
            ramu.deposit()
        elif option==2:
            ramu.withdraw()
        elif option==3:
            ramu.check_balance()
        elif option==4:
            ramu.change_pin()
        else:
            break
  
           
                
            
        
    





















      
