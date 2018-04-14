from flask import request
node = Flask(__name__)

# store the transactions that
# this node has in a list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])

def transaction():
    if request.method == 'POST':
        # on each new post request,
        # we extract the transaction data
        new_txion = request.get_json()
        # then we add the transaction to our list
        this_nodes_transactions.append(new_txion)
        # because the transaction was successfully
        # submitted, we log it to our console
        print "\n*** New transaction ***"
        print "From: {}".format(new_txion['from'])
        print "To: {}".format(new_txion['to'])
        print "Amount: {}".format(new_txion['amount'])
        # then we let the client know it worked
        return "Transaction submission successful\n"

node.run()
