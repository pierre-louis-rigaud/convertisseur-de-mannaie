from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency, history):
    c = CurrencyRates()
    valid_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR", "SGD", "NZD", "MXN", "BRL", "ZAR", "HKD"]

    try:
        amount = float(amount)
    except ValueError:
        print("Oops! Veuillez saisir un montant en numéro..")
        return

    if from_currency not in valid_currencies or to_currency not in valid_currencies:
        print("Oops! Veuillez vérifier les codes de devise. (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, SGD, NZD, MXN, BRL, ZAR, HKD)")
        return

    while c.get_rate(from_currency, to_currency) is None:
        print("Oops! Conversion impossible. Veuillez vérifier les codes de devise. (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, SGD, NZD, MXN, BRL, ZAR, HKD)")
        from_currency = input("Veuillez saisir la devise originale à nouveau : ").upper()
        to_currency = input("Veuillez saisir la devise cible à nouveau : ").upper()

    converted_amount = c.convert(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")
    history.append({'amount': amount, 'from_currency': from_currency, 'to_currency': to_currency, 'converted_amount': converted_amount})

def display_history(history):
    print("\nVoici l'historique de vos conversions :")
    for entry in history:
        print(f"{entry['amount']} {entry['from_currency']} -> {entry['converted_amount']} {entry['to_currency']}")

def main():
    conversion_history = []

    print("Liste des devises valides : USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, SGD, NZD, MXN, BRL, ZAR, HKD")

    while True:
        try:
            amount = float(input("Veuillez saisir la valeur à convertir : "))
        except ValueError:
            print("Oops! Veuillez saisir un montant numérique.")
            continue

        from_currency = input("Veuillez saisir la devise originale : ").upper()
        to_currency = input("Veuillez saisir la devise cible : ").upper()
        convert_currency(amount, from_currency, to_currency, conversion_history)
        
        another_conversion = input("Souhaitez-vous effectuer une autre conversion :) ? (Oui/Non) : ").lower()
        if another_conversion != 'oui':
            display_history(conversion_history)
            break

main()