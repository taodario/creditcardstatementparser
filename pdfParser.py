import re
from flask import Flask, request, jsonify

# sample text to match: JUL 26   JUL 26   AMZN MKTP CA*RV3W723A2 WWW.AMAZON.CAON  55490534208205344418961  $56.49

app = Flask(__name__)

pattern = re.compile(
    r'([A-Z]{3} \d{2})\s{2,}'  # matches JUL 26
    r'([A-Z]{3} \d{2})\s{2,}'  # JUL 26
    r'(.*?)\s{2,}'
    r'(\d+)\s{2,}'
    r'([\-\$\d\.\,]+)'
)


def parse_transactions(text):
    matches = pattern.findall(text)
    return [{
        'Transaction Date': m[0],
        'Posting Date': m[1],
        'Description': m[2],
        'Transaction ID': m[3],
        'Amount': m[4]
    } for m in matches]


@app.route('/parse', methods=['POST'])
def parse():
    # data = request.json
    # text = data.get('text', '')
    text = request.data.decode('utf-8')
    print("Received text: ", text)
    transactions = parse_transactions(text)
    print(transactions)
    return jsonify(transactions)


@app.route('/test', methods=['GET'])
def test():
    return "Flask is working!"


if __name__ == '__main__':
    app.run(port=5001, debug=True)

# sample_text = "RBC ®   Cash Back Mastercard J  DARIO TAO   5415 90** **** 6922 STATEMENT FROM JUL 18 TO AUG 19, 2024  2 OF 4  .  Thank you for choosing RBC Royal Bank DARIO TAO 5415 90** **** 6922 - PRIMARY (continued)  TRANSACTION POSTING   ACTIVITY DESCRIPTION   AMOUNT ($) DATE   DATE  JUL 26   JUL 29   DOMINOS PIZZA #10478 TORONTO ON  55419214209205691996433  $12.42  JUL 26   JUL 26   AMZN MKTP CA*RV3W723A2 WWW.AMAZON.CAON  55490534208205344418961  $56.49  JUL 27   JUL 29   AMZN MKTP CA WWW.AMAZON.CAON  55490534209205925976477  -$18.07  JUL 27   JUL 30   FRESHCO #3820 TORONTO ON  75259114210920266917909  $56.56  JUL 28   JUL 29   APPLE.COM/BILL 866-712-7753 ON  55490534210206079696504  $1.46  JUL 28   JUL 30   SHOPPERS DRUG MART #14 TORONTO ON  55181364211882647552315  $6.78  JUL 31   AUG 02   ACT*TOWNRICHMONDHILL RICHMOND HILLON  55181364214656620527495  $5.50  JUL 31   AUG 01   BONE SOUP MALATANG TORONTO ON  55134424213800180249444  $27.95  AUG 01   AUG 05   MCDONALD'S #29110 QPS TORONTO ON  55134424215800111406863  $3.14  AUG 01   AUG 02   TIM HORTONS #9436 TORONTO ON  55419214215207620621803  $1.67  AUG 02   AUG 02   SPOTIFY P2E337F22D STOCKHOLM SWE  15265674215000149554033  $6.77  AUG 02   AUG 02   D J*WALL-ST-JOURNAL 800-568-7625 NJ  52715974215207608710864  $2.26  AUG 02   AUG 02   PAYMENT - THANK YOU / PAIEMENT - MERCI  75105394215619986186204  -$1,024.34  AUG 03   AUG 05   IKEA NORTH YORK NORTH YORK ON  55134424216800178538573  $256.48  AUG 05   AUG 06   GOOGLE *GOOGLE ONE 650-253-0000 NS  55490534218208915014654  $3.15  AUG 06   AUG 07   PRESTO MOBL TORONTO ON  55134424219800166662820  $10.00  AUG 07   AUG 08   TIM HORTONS #2753 TORONTO ON  55419214220209582209513  $6.20  AUG 08   AUG 08   AMZN MKTP CA*RF2L56YG1 WWW.AMAZON.CAON  55490534221209706872719  $10.36  AUG 08   AUG 09   AMZN MKTP CA*RM6R73LC0 WWW.AMAZON.CAON  55490534221209925234048  $38.41  AUG 09   AUG 12   AMAZON.CA AMAZON.CA ON  55490534222200178199573  -$112.99  AUG 10   AUG 12   AMAZON.CA*RM29E2101 AMAZON.CA ON  55490534223200552188167  $13.32  AUG 10   AUG 13   FRESHCO #3820 TORONTO ON  75259114224920260896509  $51.50  AUG 11   AUG 12   POPEYE'S #12723 TORONTO ON  55419214225200985038026  $8.45  AUG 12   AUG 12   AMZN MKTP CA*RM5U255C1 WWW.AMAZON.CAON  55490534225200952270332  $11.85  AUG 12   AUG 12   AMZN MKTP CA*RM8V04830 WWW.AMAZON.CAON  55490534225200953812967  $15.88"

# matches = pattern.findall(sample_text)
#
# for match in matches:
#     print("Transaction Date: ", match[0])
#     print("Posting Date: ", match[1])
#     print("Description: ", match[2])
#     print("Transaction ID: ", match[3])
#     print("Amount: ", match[4])
#     print("-" * 40)
