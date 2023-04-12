import random
hourly_pay_rates = ("C: $16.50", "S: $15.75", "J: 15.75", "M: 19.50", )
deduction_rates = ("0.12", "0.03", "0.062", "0.0145", )

def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    global category_code, hourly_pay_rates
    category_code = int(input("Enter Category Code: "))
    hourly_pay_rates = int(input("Number of Hours Worked: "))

def perform_calculations():
    global grosspay, total, netpay
    grosspay = hourly_pay_rates * category_code
    total = grosspay * deduction_rates
    netpay = grosspay - total

def display_results():
    print("**** Fresh Food Marketplace ****")
    print(hourly_pay_rates)
    print(grosspay)
    print(total)
    print(netpay)
