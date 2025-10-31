from src.masks import get_mask_account, get_mask_card_number
from src.processing.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from src.generators.generators import card_number_generator
from src.generators.transactions import filter_by_currency, transaction_descriptions


data={
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"}

if __name__ == "__main__":
  print(get_mask_account("20000000000000000000"))
  print(get_mask_card_number("3438393009988943"))
  print(filter_by_state([{'state': 'EXECUTED'}, {'state': 'CANCELED'}, {'amount': 100}]))
  print(sort_by_date([{'date': '2024-03-01'}, {'date': '2024-01-01'}]))
  print(mask_account_card('VISA 1234567891234567'))
  print(get_date('2025-04-12T02:26:18.671407'))
  print(filter_by_currency(data, 'USD'))
  print(transaction_descriptions(data))
  print(card_number_generator(1,1000))
