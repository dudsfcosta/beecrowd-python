prod = input().split()
prod_code_1 = int(prod.pop(0))
prod_unit_1 = int(prod.pop(0))
prod_unit_price_1 = float(prod.pop(0))
prod_price_1 = prod_unit_1 * prod_unit_price_1

prod = input().split()
prod_code_2 = int(prod.pop(0))
prod_unit_2 = int(prod.pop(0))
prod_unit_price_2 = float(prod.pop(0))
prod_price_2 = prod_unit_2 * prod_unit_price_2

prod_total = prod_price_1 + prod_price_2

print(f'VALOR A PAGAR: R$ %.2f' % prod_total)