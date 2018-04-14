@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # convert our blocks into dictionaries
    # so we can send them as json objects later
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            'index': block_index,
            'timestamp': block_timestamp,
            'data': block_data,
            'hash': block_hash
        }
    # send our chain to whomever requested it
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send

def find_new_chains():
    # get the chains of every other node
    other_chains = []
    for node_url in peer_nodes:
        # get their chains using a GET request
        block = requests.get(node_url + '/blocks').content
        # convert the JSON object to a python dictionary
        block = json.loads(block)
        # add it to our list
        other_chains.append(block)
    return other_chains

def consensus():
    # get the blocks from other nodes
    other_chains = find_new_chains()
    # if our chain isn't longest,
    # then the store the longest chain
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    # if the longest chain wasn't ours,
    # then we set our chain to the longest
    blockchain = longest_chain
